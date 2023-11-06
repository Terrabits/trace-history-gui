class Controller:

    def __init__(self, model=None, view=None):
        self.model = model
        self.view  = view
        self.connect_signals_and_slots()

        # start application
        self.view.show()


    def toggle_connection(self):
        model = self.model
        view  = self.view

        # TODO: validate inputs first

        # disconnect?
        if model.is_connected:
            print('disconnecting')
            model.disconnect()
            view.disconnect()
            return

        if view.is_tcp:
            # make tcp connection
            host = view.tcp_host
            print(f'connecting to tcp endpoint {host}')  # TODO: remove
            if not model.connect_tcp(host):
                # TODO
                raise RuntimeError(f'error connecting to TCP endpoint {host}')

        else:
            # make visa connection
            resource = view.visa_resource
            print(f'connecting to visa resource {resource}')  # TODO: remove
            if not model.connect_visa(resource):
                # TODO
                raise RuntimeError(f'error connecting to VISA resource {resource}')

        # connected
        view.connect()


    def update_set_files(self):
        set_files = self.model.set_files
        self.view.update_set_files(set_files)


    def start_measurement(self):
        set_file    = self.view.set_file
        sweep_count = self.view.sweep_count
        timeout_s   = self.view.timeout_s
        data_path   = self.view.data_path
        print( 'measure and save:')
        print(f'  set_file:    {set_file}')
        print(f'  sweep_count: {sweep_count}')
        print(f'  timeout_s:   {timeout_s}')
        print(f'  data_path:   {data_path}')
        self.model.measure_and_save(set_file, sweep_count, timeout_s, data_path)


    def connect_signals_and_slots(self):
        self.view.connect_clicked.connect(self.toggle_connection)
        self.view.start_measurement_clicked.connect(self.start_measurement)
