"""Command line interface entry point."""

import typer

from .calendar.registry import DAY_REGISTRY


def run() -> None:
    """Typer app."""
    app = typer.Typer(no_args_is_help=True)
    for name, day in DAY_REGISTRY.items():
        app.command(name=name)(day)

    app()
