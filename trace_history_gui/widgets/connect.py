from .mixins.ui_mixin  import create_ui_mixin
from .ui_connect       import Ui_Connect
from PySide2.QtCore    import Slot
from PySide2.QtWidgets import QGroupBox


# constants
CONNECTED_TEXT      = 'Disconnect'
DISCONNECTED_TEXT   = 'Connect'
TCP_ENDPOINT_LABEL  = 'Host'
TCP_ENDPOINT_PAGE   = 0
VISA_ENDPOINT_LABEL = 'Resource'
VISA_ENDPOINT_PAGE  = 1


# create base class
UiMixin = create_ui_mixin(Ui_Connect, QGroupBox)


# Connect widget


class Connect(UiMixin):

    def __init__(self, parent=None):
        UiMixin.__init__(self, parent)
        self.connect_signals_and_slots()


    def connect(self):
        self.ui.methods.setDisabled(True)
        self.ui.endpointPages.setDisabled(True)
        self.ui.connect.setText(CONNECTED_TEXT)


    def disconnect(self):
        self.ui.methods.setEnabled(True)
        self.ui.endpointPages.setEnabled(True)
        self.ui.connect.setText(DISCONNECTED_TEXT)


    def connect_signals_and_slots(self):
        self.ui.isTcp.toggled.connect(self.update_endpoint_input)


    @Slot(bool)
    def update_endpoint_input(self, isTcp):
        # get label, index
        label = TCP_ENDPOINT_LABEL if isTcp else VISA_ENDPOINT_LABEL
        index = TCP_ENDPOINT_PAGE  if isTcp else VISA_ENDPOINT_PAGE

        # set page
        self.ui.endpointLabel.setText(label)
        self.ui.endpointPages.setCurrentIndex(index)
