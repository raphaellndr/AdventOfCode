"""Aoc version check."""

from src import aoc


def test_version_info():
    """Aoc version test."""
    assert aoc.__version__ is not None
