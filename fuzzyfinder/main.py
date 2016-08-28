def search(needle, haystack):
    found_index = 0
    for i, c in enumerate(needle):
        found_index = haystack.find(c, found_index)
        if found_index == -1:
            return (False, None, None)
        if i == 0:
            start = found_index
    end = found_index + 1
    return (True, start, end)

def fuzzyfinder(input, collection):
    """
    Args:
        input (str): A partial string which is typically entered by a user.
        collection (iterable): A collection of strings which will be filtered
                               based on the `input`.

    Returns:
        suggestions (generator): A generator object that produces a list of
            suggestions narrowed down from `collection` using the `input`.
    """
    suggestions = []
    input = str(input) if not isinstance(input, str) else input
    for item in collection:
        found, start, end = search(input, item)
        if found:
            suggestions.append(((end - start), start, item))

    return (x[-1] for x in sorted(suggestions))
