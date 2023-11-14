from .mixins.ui_mixin  import create_ui_mixin
from .ui_measure       import Ui_Measure
from PySide6.QtWidgets import QGroupBox


# constants
CURRENT_SET = '<Current Set>'

# create base class
UiMixin = create_ui_mixin(Ui_Measure, QGroupBox)


# Measure widget


class Measure(UiMixin):

    def __init__(self, parent=None):
        UiMixin.__init__(self, parent)
        self.ui.dataPath.save = True
        self.clear_set_files()


    # set file

    @property
    def set_file(self):
        text = self.ui.setFile.currentText()
        return self.text_to_set_file(text)


    @set_file.setter
    def set_file(self, set_file):
        text = self.set_file_to_text(set_file)
        self.ui.setFile.setCurrentText(text)


    # set files

    def clear_set_files(self):
        self.ui.setFile.clear()
        self.ui.setFile.addItem(CURRENT_SET)


    def update_set_files(self, set_files):
        # save current set file
        current_set_file = self.set_file

        # update set files
        self.clear_set_files()
        self.ui.setFile.addItems(set_files)

        # restore current set file?
        if current_set_file in set_files:
            self.ui.setFile.setCurrentText(current_set_file)


    # helpers

    @staticmethod
    def text_to_set_file(text):
        if not text:
            # default to no set file
            return None
        if text == CURRENT_SET:
            # no set file
            return None

        # text is set file
        return text


    @staticmethod
    def set_file_to_text(set_file):
        if set_file is None:
            # current set
            return CURRENT_SET
        if not set_file:
            # default to current set
            return CURRENT_SET

        # display set file
        return set_file
