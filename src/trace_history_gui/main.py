from   .command_line     import parse_args
from   .controller       import Controller
from   .model            import Model
from   .test.mock.model  import Model as MockModel
from   .widgets          import MainWindow
from   PySide6.QtWidgets import QApplication
import sys


# for inspection
app        = None
model      = None
view       = None
controller = None


def main():
    global app, controller, view, model, Model

    # parse command line args
    args = parse_args()

    # process --demo
    if args.demo:
        Model = MockModel


    # create qt app
    app = QApplication()


    # setup mvc
    model      = Model()
    view       = MainWindow()
    controller = Controller(model, view)


    # start app
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
