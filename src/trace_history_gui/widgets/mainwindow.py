from .create_property  import create_property
from .create_property  import create_property_for_attribute
from .create_property  import create_property_for_checked
from .create_property  import create_property_for_text
from .create_property  import create_property_for_visible
from .measurement_complete_dialog import MeasurementCompleteDialog
from .mixins.ui_mixin  import create_ui_mixin
from .settings         import Settings
from .timer            import Timer
from .ui_mainwindow    import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from qtrf.mixins       import ShakeMixin


# create base class
UiMixin = create_ui_mixin(Ui_MainWindow, QMainWindow)


# MainWindow


class MainWindow(ShakeMixin, UiMixin):


    # constructor

    def __init__(self, parent=None):
        super().__init__(parent)
        self.measurement_complete_dialog = MeasurementCompleteDialog(self)
        self.settings = Settings(self)
        self.timer    = Timer(self)


    # connect widget

    connect_visible = create_property_for_visible('ui.connect')


    # conection method

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

    timeout_s = create_property_for_attribute('settings.ui.timeout_s.value')


    def focus_timeout(self):
        self.ui.measure.ui.timeout_s.setFocus()
        self.ui.measure.ui.timeout_s.selectAll()


    # data path

    data_path       = create_property_for_attribute('ui.measure.ui.dataPath.file_path')
    focus_data_path = create_property_for_attribute('ui.measure.ui.dataPath.setFocus', read_only=True)


    # signal: start measurement button clicked

    start_measurement_clicked = create_property_for_attribute('ui.measure.ui.start.clicked', read_only=True)


    # signal: settings clicked

    settings_clicked = create_property_for_attribute('ui.measure.ui.settings.clicked')


    # status messages

    clear_error = create_property_for_attribute('ui.errorLabel.clear', read_only=True)


    def show_error(self, message):
        self.ui.errorLabel.show_message(message)
        self.shake()


    def show_success(self, message):
        self.ui.errorLabel.show_message(message, 'darkgreen')

    # settings dialog

    delay_s = create_property_for_attribute('settings.ui.delay_s.value')

    display_measurement_complete_dialog = create_property_for_checked('settings.ui.displayMeasurementCompleteDialog')

    open_settings_dialog = create_property_for_attribute('settings.open', read_only=True)

    settings_dialog_finished = create_property_for_attribute('settings.finished', read_only=True)

    settings_accepted = create_property_for_attribute('settings.is_accepted', read_only=True)


    # timer dialog

    start_timer = create_property_for_attribute('timer.start')

    timer_finished = create_property_for_attribute('timer.finished')

    timer_cancelled = create_property_for_attribute('timer.cancelled')


    # measurement complete dialog

    show_measurement_complete_dialog = create_property_for_attribute('measurement_complete_dialog.show', read_only=True)
