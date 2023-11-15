from   .settings_mixin import SettingsMixin
import json
from   rohdeschwarz.instruments.vna   import Vna
from   trace_history.measure_and_save import measure_and_save


class Model(SettingsMixin):


    # constructor

    def __init__(self):
        super().__init__()
        self.vna = None


    # connect / disconnect

    @property
    def is_connected(self):
        return self.vna is not None


    def connect_tcp(self, host):
        # connected?
        if self.is_connected:
            self.disconnect()

        # connect
        vna = Vna()
        try:
            vna.open_tcp(host)
        except:
            # error
            return False

        # success
        self.vna               = vna
        self.connection_method = 'tcp'
        self.tcp_host          = host
        return True


    def connect_visa(self, resource):
        # connected?
        if self.is_connected:
            self.disconnect()

        # connect
        vna = Vna()
        try:
            vna.open(resource)
        except:
            # error
            return False

        # success
        self.vna               = vna
        self.connection_method = 'visa'
        self.visa_resource     = resource
        return True


    def disconnect(self):
        if not self.is_connected:
            # already disconnected
            return

        # disconnect
        self.vna.local()
        self.vna.close()
        self.vna = None


    # vna id string

    @property
    def vna_id(self):
        return self.vna.id_string()


    # set files

    def get_set_files(self):
        return self.vna.set_files


    # measure with trace history

    def measure_and_save(self, set_file, sweep_count, timeout_s, data_path):

        # save settings
        self.set_file    = set_file
        self.sweep_count = sweep_count
        self.timeout_s   = timeout_s
        self.data_path   = str(data_path)

        # measure
        timeout_ms = timeout_s * 1000
        measure_and_save(self.vna, sweep_count, set_file, timeout_ms, data_path)
