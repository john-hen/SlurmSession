# SlurmSession
*Starts an interactive session on a compute node via Slurm.*

Can't remember the exact command plus various arguments when all you want is an
interactive shell on a compute node? Just run `slurmsession`, or `sls` for
short, and this application will prompt you for the options in the terminal.
Enter the compute resources, such as number of CPU cores and memory per core,
or quickly press <kbd>Enter</kbd> to accept the defaults, which you can
configure as needed.


## Installation

```
❯ uv tool install SlurmSession
```

This assumes you have installed the [UV] Python package manager. Alternatively,
you could use [PipX] or even the standard Python package manager Pip.

```
❯ pip install pipx
❯ pipx install SlurmSession
```

UV and PipX both isolate the dependencies of this application, so that they
will not pollute your current Python environment. The commands `slurmsession`
and `sls` will be available in the shell no matter the Python environment.


## Usage

Type `sls` or `slurmsession` to start the application, follow the prompts,
and either accept the default value by just pressing <kbd>Enter</kbd> or enter
the custom value you want instead. The remote shell session will then be
started via [Slurm] on the compute node(s). Type `exit` when done to return to
the log-in node. Run `sls --help` to see the location of the configuration
file, which you can edit to customize the defaults.

[UV]:    https://docs.astral.sh/uv
[PipX]:  https://pipx.pypa.io
[Slurm]: https://slurm.schedmd.com


[![release](
    https://img.shields.io/pypi/v/SlurmSession.svg?label=release)](
    https://pypi.python.org/pypi/SlurmSession)
[![coverage](
    https://img.shields.io/codecov/c/github/john-hen/SlurmSession)](
    https://app.codecov.io/gh/john-hen/SlurmSession)
