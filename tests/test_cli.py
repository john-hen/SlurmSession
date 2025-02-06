from slurmsession import cli
from slurmsession import config
from slurmsession import meta

from typer.testing import CliRunner
from pathlib       import Path
from subprocess    import run
from sys           import executable as python


runner = CliRunner()
defaults = Path(config.__file__).parent / 'defaults.yaml'


def test_version_is_printed():
    result = runner.invoke(cli, ['--version'])
    assert result.exit_code == 0
    assert result.stdout.strip() == meta.version


def test_help_contains_package_summary():
    result = runner.invoke(cli, ['--help'])
    assert result.exit_code == 0
    assert meta.summary in result.stdout


def test_mock_run_with_defaults():
    config.load(defaults)
    result = runner.invoke(cli, ['--mock'])
    assert result.exit_code == 0
    output = result.stdout.strip()
    assert output.startswith('Nodes')
    assert output.endswith('Type exit when done.')


def test_run_fails_with_wrong_command():
    config.load(defaults)
    config.settings['executable'] = 'command_does_not_exist_(hopefully)'
    result = runner.invoke(cli)
    assert result.exit_code == 1


def test_run_as_a_module():
    process = run(
        [python, '-m', 'slurmsession', '--version'],
        capture_output=True, text=True,
    )
    assert process.returncode == 0
    assert process.stdout.strip() == meta.version
