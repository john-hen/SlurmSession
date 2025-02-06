from slurmsession import config
from slurmsession import meta

from typer   import get_app_dir
from yaml    import safe_load
from pathlib import Path


def test_location():
    assert config.location() == Path(get_app_dir(meta.name)) / 'settings.yaml'


def test_load(tmp_path):
    file = tmp_path / 'settings.yaml'
    file.write_text('nodes: 1\n')
    config.load(file)
    assert config.settings == {'nodes': 1}


def test_init(tmp_path, monkeypatch):
    settings_file = tmp_path / 'settings.yaml'
    monkeypatch.setattr(config, 'location', lambda: settings_file)
    config.init()
    assert settings_file.exists()
    settings = safe_load(settings_file.read_text(encoding='UTF-8'))
    defaults_file = Path(config.__file__).parent / 'defaults.yaml'
    defaults = safe_load(defaults_file.read_text(encoding='UTF-8'))
    assert settings == defaults
