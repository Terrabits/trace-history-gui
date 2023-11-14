from PySide6.QtCore    import QTimer, Slot
from PySide6.QtWidgets import QLabel


# constants
MESSAGE_LIFETIME_S  = 10.0


class ErrorLabel(QLabel):

    # constructor

    def __init__(self, parent=None):
        super().__init__(parent)

        # init timer
        timer = QTimer(self)
        timer.setSingleShot(True)
        timer.setInterval(MESSAGE_LIFETIME_S * 1000)
        self.timer = timer

        # connect timer to slot
        timer.timeout.connect(self.clear)


    # message

    def show_message(self, message, color='red'):
        self.timer.start()
        self.set_color(color)
        self.setText(message)


    @Slot()
    def clear(self):
        self.timer.stop()
        QLabel.clear(self)


    # helpers

    def set_color(self, color):
        self.setStyleSheet(f'color: {color}')
