class Controller:


    # constructor

    def __init__(self, model=None, view=None):
        self.model = model
        self.view  = view

        # init view
        self.view.sweep_count = 100
        self.view.timeout_s   = 30.0
        self.view.data_path   = 'data'
        self.connect_signals_and_slots()
        self.view.show()


    # connect / disconnect

    def connect(self):
        if self.view.is_tcp:
            return self.connect_tcp()
        else:
            return self.connect_visa()


    def disconnect(self):
        self.model.disconnect()
        self.update_view()


    def handle_connect_clicked(self):
        model = self.model
        view  = self.view

        # disconnect?
        if model.is_connected:
            self.disconnect()
            return

        # validate inputs
        if not self.valid_connect_inputs():
            return

        # connect
        if not self.connect():
            # error
            return

        # success
        self.update_view()
        self.view.focus_set_file()


    def handle_start_measurement_clicked(self):
        # check for valid inputs
        if not self.valid_measure_inputs():
            return

        # start
        set_file    = self.view.set_file
        sweep_count = self.view.sweep_count
        timeout_s   = self.view.timeout_s
        data_path   = self.view.data_path
        self.model.measure_and_save(set_file, sweep_count, timeout_s, data_path)


    # helpers

    def connect_tcp(self):
        host = self.view.tcp_host
        if self.model.connect_tcp(host):
            # success
            return True
        # error
        self.view.show_error(f"error connecting to TCP endpoint '{host}'")
        return False


    def connect_visa(self):
        resource = self.view.visa_resource
        if self.model.connect_visa(resource):
            # success
            return True
        # error
        self.view.show_error(f"error connecting to VISA resource '{resource}'")
        return False


    def connect_signals_and_slots(self):
        self.view.connect_clicked.connect(self.handle_connect_clicked)
        self.view.start_measurement_clicked.connect(self.handle_start_measurement_clicked)


    def update_set_files(self):
        set_files = self.model.get_set_files()
        self.view.update_set_files(set_files)


    def update_view(self):
        # disconnected?
        if not self.model.is_connected:
            self.view.disconnect()
            return

        # connected
        self.view.connect()
        self.update_set_files()


    def valid_connect_inputs(self):
        view = self.view

        # check tcp host
        if view.is_tcp and not view.is_valid_tcp_host:
            view.show_error('*Enter valid tcp host')
            view.focus_tcp_host()
            return False

        # check visa resource
        if view.is_visa and not view.visa_resource:
            view.show_error('*Enter visa resource')
            view.focus_visa_resource()
            return False

        # valid inputs
        return True


    def valid_measure_inputs(self):
        view = self.view

        # check sweep count
        if view.sweep_count is None:
            view.show_error('*Enter sweep count')
            view.focus_sweep_count()
            return False

        # check sweep count is greater than zero
        if view.sweep_count == 0:
            view.show_error('*Sweep count must be greater than zero')
            view.focus_sweep_count()
            return False

        # check timeout
        if view.timeout_s is None:
            view.show_error('*Enter timeout')
            view.focus_timeout()
            return False

        # check timeout is greater than zero
        if view.timeout_s == 0:
            view.show_error('*Timeout must be greater than zero')
            view.focus_timeout()
            return False

        if not view.data_path:
            view.show_error('*Enter data path')
            view.focus_data_path()
            return False

        # valid inputs
        return True
