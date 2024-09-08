# -*- coding: utf-8 -*-
import re
from . import export


@export
def fuzzyfinder(input, collection, accessor=lambda x: x, sort_results=True, ignore_case=True):
    """
    Args:
        input (str): A partial string which is typically entered by a user.
        collection (iterable): A collection of strings which will be filtered
                               based on the `input`.
        accessor (function): If the `collection` is not an iterable of strings,
                             then use the accessor to fetch the string that
                             will be used for fuzzy matching.
        sort_results (bool): The suggestions are sorted by considering the
                             smallest contiguous match, followed by where the
                             match is found in the full string. If two suggestions
                             have the same rank, they are then sorted
                             alpha-numerically. This parameter controls the
                             *last tie-breaker-alpha-numeric sorting*. The sorting
                             based on match length and position will be intact.
        ignore_case (bool): If this parameter is set to False, the filtering
                            is case-sensitive.

    Returns:
        suggestions (generator): A generator object that produces a list of
            suggestions narrowed down from `collection` using the `input`.
    """
    suggestions = []
    input = str(input) if not isinstance(input, str) else input
    pat = ".*?".join(map(re.escape, input))
    pat = "(?=({0}))".format(pat)  # lookahead regex to manage overlapping matches
    regex = re.compile(pat, re.IGNORECASE if ignore_case else 0)
    for item in collection:
        r = list(regex.finditer(accessor(item)))
        if r:
            best = min(r, key=lambda x: len(x.group(1)))  # find shortest match
            suggestions.append((len(best.group(1)), best.start(), accessor(item), item))

    if sort_results:
        return (z[-1] for z in sorted(suggestions))
    else:
        return (z[-1] for z in sorted(suggestions, key=lambda x: x[:2]))
