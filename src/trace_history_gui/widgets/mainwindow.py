from .mixins.ui_mixin  import create_ui_mixin
from .ui_mainwindow    import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow


# create base class
UiMixin = create_ui_mixin(Ui_MainWindow, QMainWindow)


# MainWindow


class MainWindow(UiMixin):

    # constructor

    def __init__(self, parent=None):
        UiMixin.__init__(self, parent)


    # is tcp

    @property
    def is_tcp(self):
        return self.ui.connect.ui.isTcp.isChecked()

    @is_tcp.setter
    def is_tcp(self, checked):
        self.ui.connect.ui.isTcp.setChecked(checked)


    # is visa

    @property
    def is_visa(self):
        return self.ui.connect.ui.isVisa.isChecked()

    @is_visa.setter
    def is_visa(self, checked):
        self.ui.connect.ui.isVisa.setChecked(checked)


    # tcp host

    @property
    def tcp_host(self):
        return self.ui.connect.ui.tcpHost.text()

    @tcp_host.setter
    def tcp_host(self, host):
        self.ui.connect.ui.tcpHost.setText(host)


    # visa resource

    @property
    def visa_resource(self):
        return self.ui.connect.ui.visaResource.text()

    @visa_resource.setter
    def visa_resource(self, resource):
        self.ui.connect.ui.visaResource.setText(resource)


    # is connected

    @property
    def is_connected(self):
        return self.ui.connect.is_connected


    # signal: connect button clicked

    @property
    def connect_clicked(self):
        return self.ui.connect.ui.connect.clicked


    # connect / disconnect

    def connect(self):
        self.ui.connect.connect()
        self.ui.measure.setEnabled(True)


    def disconnect(self):
        self.ui.connect.disconnect()
        self.ui.measure.setDisabled(True)


    # set file(s)

    @property
    def set_file(self):
        return self.ui.measure.set_file

    @set_file.setter
    def set_file(self, set_file):
        self.ui.measure.set_file = set_file

    def update_set_files(self, set_files):
        self.ui.measure.update_set_files(set_files)


    # sweep count

    @property
    def sweep_count(self):
        return self.ui.measure.ui.sweepCount.value

    @sweep_count.setter
    def sweep_count(self, sweep_count):
        self.ui.measure.ui.sweepCount.value = sweep_count


    # timeout, seconds

    @property
    def timeout_s(self):
        return self.ui.measure.ui.timeout_s.value

    @timeout_s.setter
    def timeout_s(self, timeout_s):
        self.ui.measure.ui.timeout_s.value = timeout_s


    # data path

    @property
    def data_path(self):
        return self.ui.measure.ui.dataPath.filename

    @data_path.setter
    def data_path(self, data_path):
        self.ui.measure.ui.dataPath.filename = data_path


    # signal start measurement button clicked

    @property
    def start_measurement_clicked(self):
        return self.ui.measure.ui.start.clicked
