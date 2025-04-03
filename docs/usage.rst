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

Custom matching
---------------

By passing the :code:`accessor` keyword argument, you can influence how the
fuzzy matching is done. The accessor must be a function which returns a string.
This accessor function is used on each element of the collection, with the
resulting strings being used for the fuzzy matching instead of the original
elements.

Custom string matching
^^^^^^^^^^^^^^^^^^^^^^

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

Highlighting matches
--------------------

When displaying fuzzyfinder's suggestions, it is often convenient do visually
emphasize the matched substring within each suggestion. You can control such
behavior with the :code:`highlight` keyword argment.

.. note::
   Highlighting only works for collections of strings.

Highlighting in the terminal
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the terminal, characters are highlighted using ANSI escape codes. They are
inserted into individual suggestion strings, and are rendered as colors when
the string is printed.

By passing :literal:`True` to the :code:`highlight` keyword argument, the
matching substring will be highlighted in the default color (*green*).

.. code:: python

    >>> collection = ['apple', 'banana', 'grape', 'orange', 'pineapple']
    >>> suggestions = fuzzyfinder('ape', collection, highlight=True)
    >>> # Print individual elements to render highlights
    >>> list(suggestions)
    ['gr\x1b[42mape\x1b[0m', '\x1b[42map\x1b[0mpl\x1b[42me\x1b[0m', 'pine\x1b[42map\x1b[0mpl\x1b[42me\x1b[0m']

Alternatively, you can pass a string argument, which will apply highlights of
the corresponding color. Accepted values are ``'red'``, ``'green'``,
``'yellow'``, ``'blue'``, ``'magenta'``, and ``'cyan'``.

For more flexibility, see the next subsection.

Custom highlighting
^^^^^^^^^^^^^^^^^^^

You can apply custom highlighting by passing to the :code:`highlight` keyword
argument, as a :code:`tuple`, a prefix-suffix pair. The prefix and suffix are
prepended and appended to contiguous matching substring chunks, and can range
from anything like parentheses or ANSI escape codes to HTML tags with class or
style attributes.

Parentheses
"""""""""""

.. code:: python

    >>> collection = ['apple', 'banana', 'grape', 'orange', 'pineapple']
    >>> parentheses = '(', ')'
    >>> suggestions = fuzzyfinder('ape', collection, highlight=parentheses)
    >>> list(suggestions)
    ['gr(ape)', '(ap)pl(e)', 'pine(ap)pl(e)']

ANSI
""""

.. code:: python

    >>> collection = ['apple', 'banana', 'grape', 'orange', 'pineapple']
    >>> bold_with_peach_bg = "\033[48;5;209m\033[1m", "\033[0m"
    >>> suggestions = fuzzyfinder('ape', collection, highlight=bold_with_peach_bg)
    >>> list(suggestions)
    ['gr\x1b[48;5;209m\x1b[1mape\x1b[0m', '\x1b[48;5;209m\x1b[1map\x1b[0mpl\x1b[48;5;209m\x1b[1me\x1b[0m', 'pine\x1b[48;5;209m\x1b[1map\x1b[0mpl\x1b[48;5;209m\x1b[1me\x1b[0m']

HTML
""""

.. code:: python

    >>> collection = ['apple', 'banana', 'grape', 'orange', 'pineapple']
    >>> html_class = '<span class="highlight">', '</span>'
    >>> suggestions = fuzzyfinder('ape', collection, highlight=html_class)
    >>> list(suggestions)
    ['gr<span class="highlight">ape</span>', '<span class="highlight">ap</span>pl<span class="highlight">e</span>', 'pine<span class="highlight">ap</span>pl<span class="highlight">e</span>']
