from   PySide6.QtWidgets import QApplication
import sys
from   trace_history_gui.controller import Controller
from   trace_history_gui.model      import Model
from   trace_history_gui.widgets    import MainWindow


# for inspection
app        = None
model      = None
view       = None
controller = None


def main():
    global app, controller, view, model

    # create qt app
    app = QApplication([])


    # setup mvc
    model      = Model()
    view       = MainWindow()
    controller = Controller(model, view)


    # start app
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
