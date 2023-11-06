from trace_history_gui import model


class Model:

    # constructor

    def __init__(self):
        self.disconnect()


    # connect / disconnect

    @property
    def is_connected(self):
        return self.vna is not None


    def connect_tcp(self, host):
        self.method   = 'TCP'
        self.endpoint = host
        self.vna      = object()
        return self.is_connected


    def connect_visa(self, resource):
        self.method   = 'VISA'
        self.endpoint = resource
        self.vna      = object()
        return self.is_connected


    def disconnect(self):
        self.method   = None
        self.endpoint = None
        self.vna      = None
        self.set_file = None
        self.sweep_count = None
        self.timeout_s   = None
        self.data_path   = None


    # measure

    def measure_and_save(self, set_file, sweep_count, timeout_s, data_path):
        if not self.is_connected:
            raise RuntimeError('error in Model.measure(): instrument is not connected')

        # mock measure
        self.set_file    = set_file
        self.sweep_count = sweep_count
        self.timeout_s   = timeout_s
        self.data_path   = data_path


# monkeypatch

def use_mock_model():
    model.Model = Model
