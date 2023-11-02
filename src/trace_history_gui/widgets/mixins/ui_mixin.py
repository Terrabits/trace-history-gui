def create_ui_mixin(ui_class, base_class):

    class UiMixin(base_class):

        def __init__(self, parent=None):
            base_class.__init__(self, parent)
            self.ui = ui_class()
            self.ui.setupUi(self)

    return UiMixin
