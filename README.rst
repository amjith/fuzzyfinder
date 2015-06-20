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

    >>> suggestions = fuzzyfinder('abc', ['abcd', 'defabca', 'aagbec', 'xyz', 'qux'])

    >>> list(suggestions)
    ['abcd', 'defabca', 'aagbec']

Features
--------

* Simple, easy to understand code.
* No external dependencies, just the python std lib.

How does it work
----------------

TODO: Add a link to the algorithm description.

Similar Projects
----------------

* https://github.com/seatgeek/fuzzywuzzy - Fuzzy matching and auto-correction using levenshtein distance.
