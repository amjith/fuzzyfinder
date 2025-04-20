# ruff: noqa
import importlib.metadata

__version__ = importlib.metadata.version("fuzzyfinder")

__all__ = []


from typing import Callable


def export(defn: Callable) -> Callable:
    """Decorator to explicitly mark functions that are exposed in a lib."""
    globals()[defn.__name__] = defn
    __all__.append(defn.__name__)
    return defn


from . import main
