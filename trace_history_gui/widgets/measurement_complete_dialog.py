from PySide2.QtWidgets import QMessageBox


class MeasurementCompleteDialog(QMessageBox):


    # constructor

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Done')
        self.setText('Measurement is complete.')
