from   pathlib import Path
import platformdirs


# constants
APP_NAME   = "TraceHistoryGui"
APP_AUTHOR = "Rohde-Schwarz"


# paths
settings_path = Path(platformdirs.user_data_dir(APP_NAME, APP_AUTHOR))
settings_file = settings_path / 'settings.json'
