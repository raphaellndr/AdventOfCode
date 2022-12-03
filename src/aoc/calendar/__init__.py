"""Import all day."""

import importlib
from pathlib import Path

from aoc.calendar.registry import DAY_REGISTRY

__all__ = ["DAY_REGISTRY"]


for module in Path(__file__).parent.iterdir():
    if not module.is_file():
        continue

    module_name: str = str(module.stem)

    importlib.import_module(f"aoc.calendar.{module_name}")
    __all__.append(module_name)
