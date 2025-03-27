=====
Usage
=====

Start by importing :code:`fuzzyfinder` from the fuzzyfinder package:

.. code:: python

    >>> from fuzzyfinder import fuzzyfinder

Standard usage
--------------

In the standard use case, fuzzyfinder looks for ocurrences of the input string
in the elements of a collection. For an element to match, it must contain the
entire input string, with all of its characters in the same order, but not
necessarily adjacent to each other.

.. code:: python

    >>> suggestions = fuzzyfinder('abc', ['acb', 'defabca', 'abcd', 'aagbec', 'xyz', 'qux'])
    >>> list(suggestions)
    ['abcd', 'defabca', 'aagbec']

Customized matching
-------------------

By passing the :code:`accessor` keyword argument, you can influence how the
fuzzy matching is done. The accessor must be a function which returns a string.
This accessor function is used on each element of the collection, with the
resulting strings being used for the fuzzy matching instead of the original
elements.

Customized string matching
^^^^^^^^^^^^^^^^^^^^^^^^^^

Only use the second word of the string for matching.

.. code:: python

    >>> collection = ['aa bbb', 'aca xyz', 'qx ala', 'xza az', 'bc aa', 'xy abca']
    >>> suggestions = fuzzyfinder('aa', collection, accessor=lambda x: x.split()[1])
    >>> list(suggestions)
    ['bc aa', 'qx ala', 'xy abca']

Matching non-string collections
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Match integers by converting them to strings.

.. code:: python

    >>> collection = [1234, 5678, 7537, 888, 57, 77]
    >>> suggestions = fuzzyfinder('57', collection, accessor=str)
    >>> list(suggestions)
    [57, 5678, 7537]

.. note::
    Suggestions retain their original types.

Case-sensitive matching
-----------------------

By deafult, fuzzyfinder performs case-insensitive matching. To perform matching
that respects the case, you can pass :literal:`False` to the
:code:`ignore_case` keyword argument.

.. code:: python

    >>> collection = ['bAB', 'aaB', 'Aab', 'xyz', 'adb', 'aAb']
    >>> suggestions = fuzzyfinder('Ab', collection, ignore_case=False)
    >>> list(suggestions)
    ['aAb', 'Aab']

Preserving original order
-------------------------

By default, if several elements have matches of the same rank, fuzzyfinder
sorts those elements *alpha-numerically*. If you want to preserve the original
order of elements with matches of the same rank, you can pass :literal:`False`
to the :code:`sort_results` keyword argument.

.. code:: python

    >>> collection = ['aac', 'aaa', 'aba', 'xyz', 'ada']

    >>> # Alpha-numerically sort elements if matches have same rank (default)
    >>> suggestions = fuzzyfinder('aa', collection)
    >>> list(suggestions)
    ['aaa', 'aac', 'aba', 'ada']

    >>> # Preserve original order of elements if matches have same rank
    >>> suggestions = fuzzyfinder('aa', collection, sort_results=False)
    >>> list(suggestions)
    ['aac', 'aaa', 'aba', 'ada']

