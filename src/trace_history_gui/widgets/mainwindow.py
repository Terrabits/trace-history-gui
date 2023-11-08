from .create_property  import create_property
from .create_property  import create_property_for_attribute
from .create_property  import create_property_for_checked
from .create_property  import create_property_for_text
from .mixins.ui_mixin  import create_ui_mixin
from .ui_mainwindow    import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from qtrf.mixins       import ShakeMixin


# create base class
UiMixin = create_ui_mixin(Ui_MainWindow, QMainWindow)


# MainWindow


class MainWindow(ShakeMixin, UiMixin):

    # tcp or visa

    is_tcp  = create_property_for_checked('ui.connect.ui.isTcp')
    is_visa = create_property_for_checked('ui.connect.ui.isVisa')


    # tcp host

    is_valid_tcp_host = create_property('ui.connect.ui.tcpHost.hasAcceptableInput')
    tcp_host          = create_property_for_text('ui.connect.ui.tcpHost')


    def focus_tcp_host(self):
        self.ui.connect.ui.tcpHost.setFocus()
        self.ui.connect.ui.tcpHost.selectAll()


    # visa resource

    visa_resource = create_property_for_text('ui.connect.ui.visaResource')


    def focus_visa_resource(self):
        self.ui.connect.ui.visaResource.setFocus()
        self.ui.connect.ui.visaResource.selectAll()


    # signal: connect button clicked

    connect_clicked = create_property_for_attribute('ui.connect.ui.connect.clicked', read_only=True)


    # connect / disconnect

    def connect(self):
        self.ui.connect.connect()
        self.ui.measure.setEnabled(True)


    def disconnect(self):
        self.ui.connect.disconnect()
        self.ui.measure.setDisabled(True)


    # set file(s)

    set_file         = create_property_for_attribute('ui.measure.set_file')
    focus_set_file   = create_property_for_attribute('ui.measure.ui.setFile.setFocus', read_only=True)
    update_set_files = create_property_for_attribute('ui.measure.update_set_files',    read_only=True)


    # sweep count

    sweep_count = create_property_for_attribute('ui.measure.ui.sweepCount.value')


    def focus_sweep_count(self):
        self.ui.measure.ui.sweepCount.setFocus()
        self.ui.measure.ui.sweepCount.selectAll()


    # timeout, seconds

    timeout_s = create_property_for_attribute('ui.measure.ui.timeout_s.value')


    def focus_timeout(self):
        self.ui.measure.ui.timeout_s.setFocus()
        self.ui.measure.ui.timeout_s.selectAll()


    # data path

    data_path       = create_property_for_attribute('ui.measure.ui.dataPath.file_path')
    focus_data_path = create_property_for_attribute('ui.measure.ui.dataPath.setFocus', read_only=True)


    # signal: start measurement button clicked

    start_measurement_clicked = create_property_for_attribute('ui.measure.ui.start.clicked', read_only=True)


    # error messages

    clear_error = create_property_for_attribute('ui.errorLabel.clear', read_only=True)


    def show_error(self, message):
        self.ui.errorLabel.show_message(message)
        self.shake()
