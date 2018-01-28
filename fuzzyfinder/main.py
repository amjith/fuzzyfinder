# -*- coding: utf-8 -*-
import re
from . import export

@export
def fuzzyfinder(input, collection, accessor=lambda x: x):
    """
    Args:
        input (str): A partial string which is typically entered by a user.
        collection (iterable): A collection of strings which will be filtered
                               based on the `input`.
        accessor (function): If the `collection` is not an iterable of strings,
                             then use the accessor to fetch the string that
                             will be used for fuzzy matching.

    Returns:
        suggestions (generator): A generator object that produces a list of
            suggestions narrowed down from `collection` using the `input`.
    """
    suggestions = []
    input = str(input) if not isinstance(input, str) else input
    pat = '.*?'.join(map(re.escape, input))
    pat = '(?=({0}))'.format(pat)   # lookahead regex to manage overlapping matches
    regex = re.compile(pat, re.IGNORECASE)
    for item in collection:
        r = list(regex.finditer(accessor(item)))
        if r:
            best = min(r, key=lambda x: len(x.group(1)))   # find shortest match
            suggestions.append((len(best.group(1)), best.start(), accessor(item), item))

    return (z[-1] for z in sorted(suggestions))
