from   PySide6.QtWidgets import QApplication
import sys
from   trace_history_gui.widgets.mainwindow import MainWindow


# for inspection
app        = None
mainwindow = None


def main():
    global app, mainwindow

    # create qt app
    app = QApplication([])

    # create window
    mainwindow = MainWindow()
    mainwindow.show()

    # start app
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
