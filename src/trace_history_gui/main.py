from   .command_line     import parse_args
from   .controller       import Controller
from   .model            import Model
from   .test.mock.model  import Model as MockModel
from   .widgets          import MainWindow
import code
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

    # --demo?
    if args.demo:
        Model = MockModel


    # create qt app
    app = QApplication()


    # setup mvc
    model      = Model()
    view       = MainWindow()
    controller = Controller(model, view)


    # run app
    return_code = app.exec()


    # --interact?
    if args.interact:
        code.interact('', local={
            'app':   app,
            'args':  args,
            'model': model,
            'view':  view,
            'controller': controller,
        })
        sys.exit(0)

    # exit
    sys.exit(return_code)


if __name__ == '__main__':
    main()
