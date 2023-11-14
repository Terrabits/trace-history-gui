from trace_history_gui.widgets.create_property  import create_property_for_attribute


class Controller:


    # constructor

    def __init__(self, model=None, view=None):
        self.model = model
        self.view  = view

        # load saved settings
        model.load_settings()
        self.update_view()

        # init view
        self.connect_signals_and_slots()
        self.try_connect_tcp_localhost()
        view.show()


    # connect / disconnect

    def connect(self):
        # clear error messages
        self.view.clear_error()

        # validate input
        if not self.validate_connect_input():
            return False

        # connect
        if self.view.is_tcp:
            return self.connect_tcp()
        else:
            return self.connect_visa()


    def disconnect(self):
        self.view.clear_error()
        self.model.disconnect()
        self.update_view()


    def toggle_connect(self):
        model = self.model
        view  = self.view

        # disconnect?
        if model.is_connected:
            self.disconnect()
            return

        # connect
        if not self.connect():
            # error
            return

        # success
        self.view.focus_set_file()


    # start measurement

    def start_measurement(self):
        # validate input
        if not self.validate_measure_input():
            return

        # clear error messages
        self.view.clear_error()

        # start delay timer?
        delay_s = self.model.delay_s
        if delay_s:
            self.view.timer.start(delay_s)
            return

        # start now
        self.measure_and_save()


    # settings

    def open_settings_dialog(self):
        self.update_view()
        self.view.open_settings_dialog()


    # helpers

    def connect_tcp(self):
        host = self.view.tcp_host
        if not self.model.connect_tcp(host):
            # error
            self.view.show_error(f"*Error connecting to TCP endpoint '{host}'")
            return False

        # success
        self.model.save_settings()
        self.update_view()
        self.view.show_success(f'*Connected to {self.model.vna_id}')
        return True


    def connect_visa(self):
        resource = self.view.visa_resource
        if not self.model.connect_visa(resource):
            # error
            self.view.show_error(f"*Error connecting to VISA resource '{resource}'")
            return False

        # success
        self.model.save_settings()
        self.update_view()
        self.view.show_success(f'*Connected to {self.model.vna_id}')
        return True


    def measure_and_save(self):
        # measure
        self.model.measure_and_save(
            self.view.set_file,
            self.view.sweep_count,
            self.view.timeout_s,
            self.view.data_path
        )

        # success; save user settings
        self.model.save_settings()

        # show success message
        if self.model.display_measurement_complete_dialog:
            self.view.show_measurement_complete_dialog()
        else:
            self.view.show_success('*Measurement complete')


    def connect_signals_and_slots(self):
        view = self.view

        # main window
        view.connect_clicked          .connect(self.toggle_connect)
        view.start_measurement_clicked.connect(self.start_measurement)

        # settings
        view.settings_clicked         .connect(self.open_settings_dialog)
        view.settings_dialog_finished .connect(self.update_model_settings_from_view)

        # timer
        view.timer.accepted           .connect(self.measure_and_save)
        view.timer.rejected           .connect(self.show_timer_cancelled_error)


    def update_set_files(self):
        set_files = self.model.get_set_files()
        self.view.update_set_files(set_files)


    def update_model_settings_from_view(self):
        # check if user cancelled dialog
        view = self.view
        if not view.settings_accepted:
            return

        # update settings
        model         = self.model
        model.delay_s = view.delay_s
        model.display_measurement_complete_dialog = view.display_measurement_complete_dialog


    def update_view(self):
        model = self.model
        view  = self.view

        # update settings
        view.is_tcp        = model.connection_method == 'tcp'
        view.tcp_host      = model.tcp_host
        view.visa_resource = model.visa_resource
        view.delay_s       = model.delay_s
        view.display_measurement_complete_dialog = model.display_measurement_complete_dialog
        view.sweep_count   = model.sweep_count
        view.timeout_s     = model.timeout_s
        view.data_path     = model.data_path

        # disconnect?
        if not model.is_connected:
            view.disconnect()
            return

        # connected
        view.connect()
        self.update_set_files()
        view.set_file = model.set_file


    def validate_connect_input(self):
        view = self.view

        # validate tcp host
        if view.is_tcp and not view.is_valid_tcp_host:
            view.focus_tcp_host()
            view.show_error('*Enter valid tcp host')
            return False

        # validate visa resource
        if view.is_visa and not view.visa_resource:
            view.focus_visa_resource()
            view.show_error('*Enter visa resource')
            return False

        # success
        return True


    def validate_measure_input(self):
        view = self.view

        # check sweep count
        if view.sweep_count is None:
            view.focus_sweep_count()
            view.show_error('*Enter sweep count')
            return False

        # check sweep count is greater than zero
        if view.sweep_count == 0:
            view.focus_sweep_count()
            view.show_error('*Sweep count must be greater than zero')
            return False

        # check timeout
        if view.timeout_s is None:
            view.focus_timeout()
            view.show_error('*Enter timeout')
            return False

        # check timeout is greater than zero
        if view.timeout_s == 0:
            view.focus_timeout()
            view.show_error('*Timeout must be greater than zero')
            return False

        # check data path
        if not view.data_path:
            view.focus_data_path()
            view.show_error('*Enter data path')
            return False

        # success
        return True


    def show_timer_cancelled_error(self):
        self.view.show_error('*Measurement cancelled')


    def try_connect_tcp_localhost(self):
        model = self.model
        view  = self.view

        # try to connect to localhost
        if not model.connect_tcp('localhost'):
            # failed
            return

        # success; running on-instrument
        view.connect_visible = False
        self.update_view()
