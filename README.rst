===============================
fuzzyfinder
===============================

.. image:: https://img.shields.io/travis/amjith/fuzzyfinder.svg
        :target: https://travis-ci.org/amjith/fuzzyfinder

.. image:: https://img.shields.io/pypi/v/fuzzyfinder.svg
        :target: https://pypi.python.org/pypi/fuzzyfinder


Fuzzy Finder implemented in Python.

* Free software: BSD license
* Documentation: https://fuzzyfinder.readthedocs.org.

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

