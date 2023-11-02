from .mixins.ui_mixin  import create_ui_mixin
from .ui_mainwindow    import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow


# create base class
UiMixin = create_ui_mixin(Ui_MainWindow, QMainWindow)


# MainWindow


class MainWindow(UiMixin):
    pass
