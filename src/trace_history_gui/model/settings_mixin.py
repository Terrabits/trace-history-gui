from   ..paths import settings_file, settings_path
import json
from   pathlib import Path


# constants
ATTRIBUTES = [
    'connection_method',
    'tcp_host',
    'visa_resource',
    'delay_s',
    'display_measurement_complete_dialog',
    'set_file',
    'sweep_count',
    'timeout_s',
    'data_path',
]
DEFAULT_DATA_PATH = str(Path('data').resolve())
FIVE_MINUTES_S = 5 * 60


class SettingsMixin:


    # constructor

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # default settings
        self.connection_method = None
        self.tcp_host          = None
        self.visa_resource     = None
        self.delay_s           = 0
        self.display_measurement_complete_dialog = False
        self.set_file          = '<Current Set>'
        self.sweep_count       = 10
        self.timeout_s         = FIVE_MINUTES_S
        self.data_path         = DEFAULT_DATA_PATH


    # load

    def load_settings(self):
        if not settings_file.exists() or not settings_file.is_file():
            # nothing to load
            return

        # load
        with settings_file.open() as f:
            self.settings = json.load(f)


    # save

    def save_settings(self):
        settings_path.mkdir(parents=True, exist_ok=True)
        with settings_file.open('w') as f:
            json.dump(self.settings, f)


    # delete

    @staticmethod
    def delete_settings_file():
        settings_file.unlink(missing_ok=True)


    # helpers

    @property
    def settings(self):
        settings = {}
        for attr in ATTRIBUTES:
            print(f'settings[{attr}] = {getattr(self, attr)}')
            settings[attr] = getattr(self, attr)
        return settings


    @settings.setter
    def settings(self, settings):
        for attr, value in settings.items():
            print(f'self.{attr} = {value}')
            setattr(self, attr, value)
