===========
fuzzyfinder
===========

.. image:: https://img.shields.io/pypi/v/fuzzyfinder.svg
   :target: https://pypi.python.org/pypi/fuzzyfinder

.. image:: https://img.shields.io/badge/github-fuzzyfinder-brightgreen?logo=github
   :alt: GitHub Badge
   :target: https://github.com/amjith/fuzzyfinder

.. image:: https://img.shields.io/badge/docs-fuzzyfinder-hotpink?logo=readthedocs&logoColor=white
   :alt: ReadTheDocs Badge
   :target: https://fuzzyfinder.readthedocs.io/


**fuzzyfinder** is a fuzzy finder implemented in Python. It matches partial
string entries from a list of strings, and works similar to the fuzzy finder in
SublimeText and Vim's Ctrl-P plugin.

.. image:: https://raw.githubusercontent.com/amjith/fuzzyfinder/master/screenshots/highlight-demo.gif

Some notable features of fuzzyfinder are:

* **Simple**, easy to understand code.
* **No external dependencies**, just the Python standard library.

An in-depth overview of the algorithm behind fuzzyfinder is available in
`this blog post`__.

__ http://blog.amjith.com/fuzzyfinder-in-10-lines-of-python

Quick Start
-----------

Installation
^^^^^^^^^^^^
::

    $ pip install fuzzyfinder

Usage
^^^^^

.. code:: python

    >>> from fuzzyfinder import fuzzyfinder

    >>> suggestions = fuzzyfinder('abc', ['acb', 'defabca', 'abcd', 'aagbec', 'xyz', 'qux'])
    >>> list(suggestions)
    ['abcd', 'defabca', 'aagbec']

    >>> # Use a user-defined function to obtain the string against which fuzzy matching is done
    >>> collection = ['aa bbb', 'aca xyz', 'qx ala', 'xza az', 'bc aa', 'xy abca']
    >>> suggestions = fuzzyfinder('aa', collection, accessor=lambda x: x.split()[1])
    >>> list(suggestions)
    ['bc aa', 'qx ala', 'xy abca']

    >>> # With the appropriate accessor you can pass non-string collections, too
    >>> collection = [1234, 5678, 7537, 888, 57, 77]
    >>> suggestions = fuzzyfinder('57', collection, accessor=str)
    >>> list(suggestions)
    [57, 5678, 7537]

    >>> # Make filtering case-sensitive
    >>> collection = ['bAB', 'aaB', 'Aab', 'xyz', 'adb', 'aAb']
    >>> suggestions = fuzzyfinder('Ab', collection, ignore_case=False)
    >>> list(suggestions)
    ['aAb', 'Aab']

    >>> # By default, elements with matches of same rank are sorted alpha-numerically
    >>> suggestions = fuzzyfinder('aa', ['aac', 'aaa', 'aab', 'xyz', 'ada'])
    >>> list(suggestions)
    ['aaa', 'aab', 'aac', 'ada']

    >>> # Preserve original order of elements if matches have same rank
    >>> suggestions = fuzzyfinder('aa', ['aac', 'aaa', 'aab', 'xyz', 'ada'], sort_results=False)
    >>> list(suggestions)
    ['aac', 'aaa', 'aab', 'ada']

    >>> # Highlight matching substrings when printing to the terminal
    >>> collection = ['apple', 'banana', 'grape', 'orange', 'pineapple']
    >>> suggestions = fuzzyfinder('ape', collection, highlight=True)
    >>> list(suggestions)
    ['gr\x1b[42mape\x1b[0m', '\x1b[42map\x1b[0mpl\x1b[42me\x1b[0m', 'pine\x1b[42map\x1b[0mpl\x1b[42me\x1b[0m']

    >>> # Custom highlighting (use with ANSI, HTML, etc.)
    >>> parentheses = '(', ')'
    >>> suggestions = fuzzyfinder('ape', collection, highlight=parentheses)
    >>> list(suggestions)
    ['gr(ape)', '(ap)pl(e)', 'pine(ap)pl(e)']

Similar Projects
----------------

* https://github.com/seatgeek/thefuzz - Fuzzy matching and auto-correction using levenshtein distance.
