"""Handles configuration options and storage."""

from . import meta

from yaml    import safe_load
from typer   import get_app_dir
from pathlib import Path
from shutil  import copy2 as copy


settings = {}


def location() -> Path:
    """Returns the platform-dependent location of the configuration file."""
    return Path(get_app_dir(meta.name)) / 'settings.yaml'


def load(file: Path):
    """Loads configuration from `file`."""
    global settings
    with file.open(encoding='UTF-8') as stream:
        settings = safe_load(stream)


def init():
    """Loads configuration or initializes with defaults if missing."""
    file = location()
    if not file.exists():
        here = Path(__file__).parent
        defaults = here/'defaults.yaml'
        file = location()
        file.parent.mkdir(exist_ok=True)
        copy(defaults, file)
    load(file)


# Initialize when app starts.
init()
