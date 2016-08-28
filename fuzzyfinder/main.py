def make_searcher(query):
    if len(query) == 0:
        return lambda x: (True, 0, 0)

    head = query[0]
    tail = query[1:]

    def matcher(datum):
        running = 0
        first = datum.find(head)
        if first == -1:
            return (False, -1, -1)
        datum = datum[first+1:]

        for char in tail:
            index = datum.find(char)
            if index == -1:
                return (False, -1, -1)
            running += index
            datum = datum[index+1:]

        return (True, running, first)

    return matcher


def fuzzyfinder(query, data):
    suggestions = []
    searcher = make_searcher(query)

    for item in data:
        matched, distance, first = searcher(item)
        if not matched:
            continue
        suggestions.append((distance, first, item))
    return [x for _, _, x in sorted(suggestions)]
