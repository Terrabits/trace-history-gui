class Controller:

    def __init__(self, model=None, view=None):
        self.model = model
        self.view  = view

        # init view
        self.view.sweep_count = 100
        self.view.timeout_s   = 30.0
        self.view.data_path   = 'data'
        self.connect_signals_and_slots()
        self.view.show()


    def toggle_connection(self):
        model = self.model
        view  = self.view


        # disconnect?
        if model.is_connected:
            print('disconnecting')
            model.disconnect()
            self.update_view()
            return


        # connect

        # validate inputs
        if not self.valid_connect_inputs():
            return

        # make tcp connection?
        if view.is_tcp:
            # make tcp connection
            host = view.tcp_host
            print(f'connecting to tcp endpoint {host}')  # TODO: remove
            if not model.connect_tcp(host):
                # TODO
                print(f'error connecting to TCP endpoint {host}')
                return


        # make visa connection?
        else:
            # make visa connection
            resource = view.visa_resource
            print(f'connecting to visa resource {resource}')  # TODO: remove
            if not model.connect_visa(resource):
                # TODO
                print(f'error connecting to VISA resource {resource}')
                return


        # connected
        self.update_view()
        self.view.focus_set_file()


    def start_measurement(self):
        # validate inputs
        if not self.valid_measure_inputs():
            return
        set_file    = self.view.set_file
        sweep_count = self.view.sweep_count
        timeout_s   = self.view.timeout_s
        data_path   = self.view.data_path
        print( 'measure and save:')
        print(f'  set_file:    {set_file}')
        print(f'  sweep_count: {sweep_count}')
        print(f'  timeout_s:   {timeout_s}')
        print(f'  data_path:   {data_path.name}')
        self.model.measure_and_save(set_file, sweep_count, timeout_s, data_path)


    # helpers

    def connect_signals_and_slots(self):
        self.view.connect_clicked.connect(self.toggle_connection)
        self.view.start_measurement_clicked.connect(self.start_measurement)


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
            print('error: enter valid tcp host')
            view.focus_tcp_host()
            view.shake()
            return False

        # check visa resource
        if view.is_visa and not view.visa_resource:
            # TODO
            print('error: enter visa resource')
            view.focus_visa_resource()
            view.shake()
            return False

        # valid inputs
        return True


    def valid_measure_inputs(self):
        view = self.view

        # check sweep count
        if view.sweep_count is None:
            print('error: enter sweep count')
            view.focus_sweep_count()
            view.shake()
            return False

        # check sweep count is greater than zero
        if view.sweep_count == 0:
            print('error: sweep count must be greater than zero')
            view.focus_sweep_count()
            view.shake()
            return False

        # check timeout
        if view.timeout_s is None:
            print('error: enter timeout')
            view.focus_timeout()
            view.shake()
            return False

        # check timeout is greater than zero
        if view.timeout_s == 0:
            print('error: timeout must be greater than zero')
            view.focus_timeout()
            view.shake()
            return False

        if not view.data_path:
            print('error: enter data path')
            view.focus_data_path()
            view.shake()
            return False

        # valid inputs
        return True
