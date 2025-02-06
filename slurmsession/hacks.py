"""Hacky code, avert eyes."""

from . import meta

import typer


class TyperAppWithHelpProlog(typer.core.TyperGroup):
    """
    Custom class that adds a prolog before the usage information.

    Typer does not support this feature out of the box. We therefore implement
    it ourselves, even though it's a bit hacky, what with the prolog text being
    hard-coded in the class definition below.

    Adapted from the code suggested in the corresponding GitHub issue:
    https://github.com/fastapi/typer/issues/537
    """

    def get_usage(self, context: typer.Context) -> str:
        usage  = super().get_usage(context)
        prolog = f'{meta.name}: {meta.summary}'
        return prolog + '\n\n' + usage


# Typer displays the main help text (the one that appears right after the
# usage), except for its very  first line (deemed the most important),
# in a difficult-to-read gray ("dimmed"). It's a hard-coded style, so all
# we can do is monkey-patch it.
typer.rich_utils.STYLE_HELPTEXT = ''
