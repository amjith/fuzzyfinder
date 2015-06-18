# -*- coding: utf-8 -*-
import re
from . import export

@export
def fuzzyfinder(text, collection):
    """
    Args:
        text (str): A partial string which is typically entered by a user.
        collection (iterable): A collection of strings which will be filtered
                               based on the input `text`.

    Returns:
        suggestions (generator): A generator object that produces a list of
            suggestions narrowed down from `collections` using the `text`
            input.
    """
    suggestions = []
    regex = '.*?'.join(map(re.escape, text))
    pat = re.compile('%s' % regex)
    for item in sorted(collection):
        r = pat.search(item)
        if r:
            suggestions.append((len(r.group()), r.start(), item))

    return (z for _, _, z in sorted(suggestions))
