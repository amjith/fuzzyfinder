========
Usage
========

To use fuzzyfinder in a project::

    from fuzzyfinder import fuzzyfinder

    collection = ['abcd', 'defabca', 'aagbec', 'xyz', 'qux']

    suggestions = fuzzyfinder('abc', collection)

    print list(suggestions)
