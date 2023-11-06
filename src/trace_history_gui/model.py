from rohdeschwarz.instruments.vna import Vna
from trace_history import measure_and_save


class Model:


    def __init__(self):
        self.vna = None


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
        self.vna = vna
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
        self.vna = vna
        return True


    def disconnect(self):
        if not self.is_connected:
            # already disconnected
            return

        # disconnect
        self.vna.close()
        self.vna = None


    def measure_and_save(self, set_file, sweep_count, timeout_s, data_path):
        measure_and_save()