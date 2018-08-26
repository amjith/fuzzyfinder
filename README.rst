===============================
fuzzyfinder
===============================

.. image:: https://img.shields.io/travis/amjith/fuzzyfinder.svg
        :target: https://travis-ci.org/amjith/fuzzyfinder

.. image:: https://img.shields.io/pypi/v/fuzzyfinder.svg
        :target: https://pypi.python.org/pypi/fuzzyfinder


Fuzzy Finder implemented in Python. Matches partial string entries from a list
of strings. Works similar to fuzzy finder in SublimeText and Vim's Ctrl-P
plugin.

* Documentation: https://fuzzyfinder.readthedocs.org.
* Source: https://github.com/amjith/fuzzyfinder

.. image:: https://raw.githubusercontent.com/amjith/fuzzyfinder/master/screenshots/pgcli-fuzzy.gif

Quick Start
-----------

::

    $ pip install fuzzyfinder

    or

    $ easy_install fuzzyfinder

Usage
-----

::

    >>> from fuzzyfinder import fuzzyfinder

    >>> suggestions = fuzzyfinder('abc', ['defabca', 'abcd', 'aagbec', 'xyz', 'qux'])
    >>> list(suggestions)
    ['abcd', 'defabca', 'aagbec']

    >>> # Use a user-defined function to obtain the string against which fuzzy matching is done
    >>> collection = ['aa bbb', 'aca xyz', 'qx ala', 'xza az', 'bc aa', 'xy abca']
    >>> suggestions = fuzzyfinder('aa', collection, accessor=lambda x: x.split()[1])
    >>> list(suggestions)
    ['bc aa', 'qx ala', 'xy abca']

    >>> suggestions = fuzzyfinder('aa', ['aac', 'aaa', 'aab', 'xyz', 'ada'])
    >>> list(suggestions)
    ['aaa', 'aab', 'aac', 'ada']

    >>> # Preserve original order of elements if matches have same rank
    >>> suggestions = fuzzyfinder('aa', ['aac', 'aaa', 'aab', 'xyz', 'ada'], sort_results=False)
    >>> list(suggestions)
    ['aac', 'aaa', 'aab', 'ada']

Features
--------

* Simple, easy to understand code.
* No external dependencies, just the python std lib.

How does it work
----------------

Blog post describing the algorithm: http://blog.amjith.com/fuzzyfinder-in-10-lines-of-python

Similar Projects
----------------

* https://github.com/seatgeek/fuzzywuzzy - Fuzzy matching and auto-correction using levenshtein distance.
