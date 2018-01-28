# -*- coding: utf-8 -*-

__author__ = 'Amjith Ramanujam'
__email__ = 'amjith.r@gmail.com'
__version__ = '2.1.0'

__all__ = []

def export(defn):
    """Decorator to explicitly mark functions that are exposed in a lib."""
    globals()[defn.__name__] = defn
    __all__.append(defn.__name__)
    return defn

from . import main
