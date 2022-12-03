"""Day decorator."""

from typing import Callable, MutableMapping

DAY_REGISTRY: MutableMapping[str, Callable] = {}


def day(func: Callable = None, *, name: str = None) -> Callable:  # type:ignore
    """
    :param func:
    :param name:
    :return:
    """

    def _decorator(target: Callable) -> Callable:
        nonlocal name

        name = name or target.__name__
        DAY_REGISTRY[name] = target
        return target

    if func is not None:
        return _decorator(func)
    return _decorator


__all__ = ["DAY_REGISTRY", "day"]
