"""Exposes the command-line interface."""

from . import config
from . import meta
from . import hacks

import typer
import rich
import textwrap
import subprocess
import sys


def help() -> str:
    text = textwrap.dedent(f"""
        Call without arguments to be prompted for the options.
        <html><br/></html>

        Configure default values in `{config.location()}`.
    """)
    # The HTML snippet is an ugly hack to add a blank line in the help output.
    # Otherwise Typer would smoosh the paragraphs together.
    return text


cli = typer.Typer(
    cls=hacks.TyperAppWithHelpProlog,
    add_completion=False,
    rich_markup_mode='markdown',
    help=help(),
)


def message(text: str):
    """Displays a message to the user, possibly formatted in Markdown."""
    rich.print(rich.markdown.Markdown(text))


def abort(message: str, exit_code: int = 1):
    """Displays an error message in red bold."""
    rich.print(f'[bold red]{message}[/bold red]', file=sys.stderr)
    raise typer.Exit(exit_code)


def version(flag: bool):
    """Show version number and exit."""
    if flag:
        print(meta.version)
        raise typer.Exit


def default_nodes() -> int:
    return config.settings['nodes']


def default_tasks() -> int:
    return config.settings['tasks']


def default_cores() -> int:
    return config.settings['cores']


def default_memory() -> str:
    return config.settings['memory']


def default_time() -> str:
    return config.settings['time']


@cli.callback(invoke_without_command=True, help=help)
def main(
    nodes:   int  = typer.Option(default_nodes,  prompt=True),
    tasks:   int  = typer.Option(default_tasks,  prompt=True),
    cores:   int  = typer.Option(default_cores,  prompt=True),
    memory:  str  = typer.Option(default_memory, prompt=True),
    time:    str  = typer.Option(default_time,   prompt=True),
    version: bool = typer.Option(             # noqa: ARG001 (unused argument)
       False, '--version', callback=version, help=version.__doc__,
    ),
    mock:    bool = typer.Option(False, hidden=True),  # Used in testing.
):
    command = [
        config.settings['executable'],
        *config.settings['arguments'],
        f'--nodes={nodes}',
        f'--ntasks={tasks}',
        f'--cpus-per-task={cores}',
        f'--mem-per-cpu={memory}',
        f'--time={time}',
        config.settings['shell'],
    ]
    message('Starting remote shell via Slurm.')
    message(f'Running command: `{" ".join(command)}`')
    message('Type `exit` when done.')
    if mock:
        raise typer.Exit(0)
    try:
        subprocess.run(command)
    except Exception as error:
        abort(str(error))
