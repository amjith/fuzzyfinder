# -*- coding: utf-8 -*-
from typing import Iterable, Iterator, Callable, Any
import re
from . import export


@export
def fuzzyfinder(
    input: str, collection: Iterable[Any], accessor: Callable[[Any], str] = lambda x: x, sort_results: bool = True, ignore_case: bool = True
) -> Iterator[Any]:
    """Filter a collection of objects by fuzzy matching against an input string.

    Args:
        input:
            A partial string which is typically entered by a user.
        collection:
            An iterable of objects which will be filtered based on the
            ``input``. If the objects are not strings, an appropriate
            ``accessor`` keyword argument must be passed.
        accessor:
            If the ``collection`` is not an iterable of strings, then use the
            accessor to fetch the string that will be used for fuzzy matching.
            Defaults to the identity function (simply returns the argument it
            received as input).
        sort_results:
            The suggestions are sorted by considering the smallest contiguous
            match, followed by where the match is found in the full string. If
            two suggestions have the same rank, they are then sorted
            alpha-numerically. This parameter controls the
            *last tie-breaker-alpha-numeric sorting*. The sorting based on
            match length and position will be intact.
            Defaults to ``True``.
        ignore_case:
            If this parameter is set to ``False``, the filtering is
            case-sensitive.
            Defaults to ``True``.

    Returns:
        Iterator[Any]:
            A generator object that produces a list of suggestions narrowed
            down from ``collection`` using the ``input``.

    Example:
        >>> suggestions = fuzzyfinder('abc', ['acb', 'defabca', 'abcd', 'aagbec', 'xyz', 'qux'])
        >>> list(suggestions)
        ['abcd', 'defabca', 'aagbec']
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
