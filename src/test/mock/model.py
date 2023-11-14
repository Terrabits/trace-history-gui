from trace_history_gui.model.settings_mixin import SettingsMixin


class Model(SettingsMixin):


    # constructor

    def __init__(self):

        # init settings
        super().__init__()

        # init mock vna properties
        self.vna_id    = 'Rohde-Schwarz,ZNB8-2Port,1311601042100005,1.30.12'
        self.set_files = ['MySet1.znx', 'MySet2.znx', 'MySet3.znx']

        # start disconnected
        self.disconnect()


    # connect / disconnect

    @property
    def is_connected(self):
        return self.vna is not None


    def connect_tcp(self, host):

        # connect
        self.vna = object()

        # success
        self.connection_method = 'tcp'
        self.tcp_host          = host
        return True


    def connect_visa(self, resource):

        # connect
        self.vna = object()

        # success
        self.connection_method = 'visa'
        self.visa_resource     = resource
        return True


    def disconnect(self):
        self.vna = None


    # set files

    def get_set_files(self):
        return self.set_files


    # measure

    def measure_and_save(self, set_file, sweep_count, timeout_s, data_path):
        if not self.is_connected:
            raise RuntimeError('error in Model.measure(): instrument is not connected')

        # mock measure
        self.set_file    = set_file
        self.sweep_count = sweep_count
        self.timeout_s   = timeout_s
        self.data_path   = str(data_path)
