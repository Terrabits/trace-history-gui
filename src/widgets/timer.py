from .create_property  import create_property_for_attribute
from .mixins.ui_mixin  import create_ui_mixin
from .ui_timer         import Ui_Timer
from math              import ceil
from PySide6.QtCore    import Signal, Slot, Qt, QTimer
from PySide6.QtWidgets import QDialog


# constants
ONE_SECOND = 1000

# create base class
UiMixin = create_ui_mixin(Ui_Timer, QDialog)


# Timer


class Timer(UiMixin):


    # constructor

    def __init__(self, parent=None):
        super().__init__(parent)

        # maximize
        self.setWindowState(Qt.WindowMaximized)

        # init display
        self.time_s = 0
        self.update_display()

        # init timer
        self.timer = QTimer(self)
        self.timer.setInterval(ONE_SECOND)
        self.connect_signals_and_slots()


    # start

    def start(self, time_s):
        self.time_s = ceil(time_s)
        self.update_display()
        self.timer.start()
        self.open()


    # result

    @property
    def cancelled(self):
        return self.result() == QDialog.Rejected


    # helpers

    @property
    def minutes(self):
        return self.time_s // 60


    @property
    def seconds(self):
        return self.time_s - self.minutes * 60


    def update_display(self):
        lcd = self.ui.lcd
        lcd.display(f'{self.minutes:02}:{self.seconds:02}')


    @Slot()
    def decrement_and_display(self):
        # decrement
        self.time_s -= 1

        # display
        self.update_display()

        # is time up?
        if self.time_s <= 0:
            self.timer.stop()
            self.accept()
            return


    def connect_signals_and_slots(self):
        self.timer.timeout.connect(self.decrement_and_display)
        self.finished.connect(self.timer.stop)
