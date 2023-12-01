def create_ui_mixin(ui_class, base_class):

    class UiMixin(base_class):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.ui = ui_class()
            self.ui.setupUi(self)

    return UiMixin
