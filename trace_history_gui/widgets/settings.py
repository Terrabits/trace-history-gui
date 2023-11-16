from .create_property  import create_property_for_attribute
from .create_property  import create_property_for_checked
from .mixins.ui_mixin  import create_ui_mixin
from .ui_settings      import Ui_Settings
from PySide2.QtWidgets import QDialog


# create base class
UiMixin = create_ui_mixin(Ui_Settings, QDialog)


# Settings


class Settings(UiMixin):


    # constructor

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui.delay_s.decimal_places   = 0
        self.ui.timeout_s.decimal_places = 0
        self.ui.cancel.clicked.connect(self.reject)
        self.ui.ok.clicked.connect(self.accept)


    # properties

    @property
    def is_accepted(self):
        return self.result() == QDialog.Accepted
