from .mixins.ui_mixin  import create_ui_mixin
from .ui_mainwindow    import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow
from qtrf.mixins       import ShakeMixin


# create base class
UiMixin = create_ui_mixin(Ui_MainWindow, QMainWindow)


# MainWindow


class MainWindow(ShakeMixin, UiMixin):

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
    def is_valid_tcp_host(self):
        return self.ui.connect.ui.tcpHost.hasAcceptableInput()


    @property
    def tcp_host(self):
        return self.ui.connect.ui.tcpHost.text() or None


    @tcp_host.setter
    def tcp_host(self, host):
        tcp_host = self.ui.connect.ui.tcpHost
        tcp_host.setText(host.strip() or '')


    def focus_tcp_host(self):
        tcp_host = self.ui.connect.ui.tcpHost
        tcp_host.setFocus()
        tcp_host.selectAll()


    # visa resource

    @property
    def visa_resource(self):
        return self.ui.connect.ui.visaResource.text().strip() or None


    @visa_resource.setter
    def visa_resource(self, resource):
        visa_resource = self.ui.connect.ui.visaResource
        visa_resource.setText(resource.strip() or '')


    def focus_visa_resource(self):
        visa_resource = self.ui.connect.ui.visaResource
        visa_resource.setFocus()
        visa_resource.selectAll()


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


    def focus_set_file(self):
        self.ui.measure.ui.setFile.setFocus()


    # sweep count

    @property
    def sweep_count(self):
        return self.ui.measure.ui.sweepCount.value


    @sweep_count.setter
    def sweep_count(self, sweep_count):
        self.ui.measure.ui.sweepCount.value = sweep_count


    def focus_sweep_count(self):
        sweep_count = self.ui.measure.ui.sweepCount
        sweep_count.setFocus()
        sweep_count.selectAll()


    # timeout, seconds

    @property
    def timeout_s(self):
        return self.ui.measure.ui.timeout_s.value


    @timeout_s.setter
    def timeout_s(self, timeout_s):
        self.ui.measure.ui.timeout_s.value = timeout_s


    def focus_timeout(self):
        timeout = self.ui.measure.ui.timeout_s
        timeout.setFocus()
        timeout.selectAll()


    # data path

    @property
    def data_path(self):
        return self.ui.measure.ui.dataPath.file_path


    @data_path.setter
    def data_path(self, data_path):
        self.ui.measure.ui.dataPath.file_path = data_path


    def focus_data_path(self):
        self.ui.measure.ui.dataPath.setFocus()


    # signal start measurement button clicked

    @property
    def start_measurement_clicked(self):
        return self.ui.measure.ui.start.clicked
