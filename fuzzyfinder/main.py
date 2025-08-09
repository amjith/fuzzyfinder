# -*- coding: utf-8 -*-
import operator
from typing import Any, Callable, Iterable, Iterator, Optional, Tuple, Union
import re
from . import export


COLORS_TO_ANSI = {
    "red": "\033[41m",
    "green": "\033[42m",
    "yellow": "\033[43m",
    "blue": "\033[44m",
    "magenta": "\033[45m",
    "cyan": "\033[46m",
}
ANSI_RESET = "\033[0m"


def highlight_substring(
    substring: str,
    string: str,
    highlight: Union[bool, str, Tuple[str, str]],
    ignore_case: bool,
) -> str:
    """Apply `highlight` to contiguous chunks of `substring` within `string`."""
    assert highlight, "called function when 'highlight' was falsy"
    default_highlight = "green"
    if highlight is True:
        highlight = default_highlight
    if isinstance(highlight, str):
        if not (ansi_code := COLORS_TO_ANSI.get(highlight.lower())):
            raise ValueError(f"highlight, if a string, must be one of: {str(list(COLORS_TO_ANSI)).strip('[]')}")
        highlight = ansi_code, ANSI_RESET
    assert isinstance(highlight, tuple), "incorrect type for 'highlight'"

    # We apply to the main string, pairwise, styling prefixes and suffixes
    # which mark the matched substring. We iterate over both the main string
    # and the substring exactly once, and make sure that prefix-suffix pairs
    # wrap entire chunks of adjacent matched characters as opposed to each
    # character individually.
    prefix, suffix = highlight
    highlighted_string = ""
    # We use an iterator for iterating over the main string. This ensures that:
    # (1) for each substring character, we start iteration where we stopped for
    # the previous substring character;
    # (2) after matching the final substring character, the remainder of the
    # main string's characters is preserved within the iterator.
    string_iter = iter(string)
    unpaired_prefix = False
    for substring_char in substring:
        for string_char in string_iter:
            match = string_char == substring_char
            case_insensitive_match = string_char.lower() == substring_char.lower()
            if match or (ignore_case and case_insensitive_match):
                if not unpaired_prefix:
                    highlighted_string += prefix
                    unpaired_prefix = True
                highlighted_string += string_char
                break
            else:
                if unpaired_prefix:
                    highlighted_string += suffix
                    unpaired_prefix = False
                highlighted_string += string_char
    # If the final match is between the last characters of both strings,
    # a prefix is left unpaired, so we check for it here.
    if unpaired_prefix:
        highlighted_string += suffix
    remainder = "".join(string_iter)
    highlighted_string += remainder
    return highlighted_string


@export
def fuzzyfinder(
    input: str,
    collection: Iterable[Any],
    accessor: Optional[Callable[[Any], str]] = None,
    sort_results: bool = True,
    ignore_case: bool = True,
    highlight: Union[bool, str, Tuple[str, str]] = False,
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
        highlight:
            Highlight the matching substrings when printed to the terminal, or
            elsewhere.
            If ``True``, when printed to the terminal, the matching substrings
            will have the default highlight (*green*).
            If this parameter is a ``str``, when printed to the terminal, the
            matching substrings will be highlighted in the corresponding color.
            Accepted values are: ``'red'``, ``'green'``, ``'yellow'``,
            ``'blue'``, ``'magenta'``, and ``'cyan'``.
            If this parameter is a ``tuple``, it must be a 2-tuple consisting
            of a prefix and a suffix string. The prefix and suffix are
            prepended  and appended to contiguous substring chunks, and can
            range from anything like parentheses or ANSI escape codes to HTML
            tags with class or style attributes.
            Defaults to ``False``.

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
        accessed_item = item if accessor is None else accessor(item)
        r = tuple(regex.finditer(accessed_item))
        if r:
            best = min(r, key=lambda x: len(x.group(1)))  # find shortest match
            suggestions.append((len(best.group(1)), best.start(), accessed_item, item))

    if sort_results:
        suggestions.sort()
    else:
        suggestions.sort(key=lambda x: x[:2])
    results: Iterator[Any] = map(operator.itemgetter(-1), suggestions)

    if highlight:
        results = (highlight_substring(input, result, highlight, ignore_case) for result in results)

    return results
