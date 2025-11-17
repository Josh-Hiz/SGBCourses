Defining Lists
==============

Another kind of data beyond numbers, strings, and booleans that comes up often in programming is *collections* of data. For example, one component of a course in Webreg is a collection of students. A playlist is a collection of songs. A shopping cart on a web site is a collection of items. A text conversation is a collection of messages, and so on.

In Python, a common way to represent collections of data is with lists. Here's a list in Python:

.. code-block::

    >>> some_numbers = [46, 12, 3, 9]
    >>> some_numbers
    [46, 12, 3, 9]

Like we're used to seeing with other datatypes, list values can be stored in variables, and when we ask Python for their value at the prompt, Python prints them out.

When we write down a list in Python, we can write it as comma-separated expressions in between square brackets ``[ ]``. Note that the values in a list are allowed to be expressions (just like function arguments or operands in an arithmetic/logical expression):

.. code-block::

    >>> x = 9
    >>> [x, x + 3, 7]
    [9, 12, 7]

Lists can contain any Python datatype – they can contain strings or booleans, too (they can also contain other lists, which we won't use right away).

.. code-block:: 

    >>> shopping_list = ["milk", "oranges", "rice"]
    >>> shopping_list
    ['milk', 'oranges', 'rice']

List Functions
--------------

There are a number of functions defined that work with lists. For example, the function ``len`` works not just on strings, but on lists, too! It reports the number of elements in the list:

.. code-block:: 

    >>> some_numbers = [46, 12, 3, 9]
    >>> len(some_numbers)
    4

Here's another example:

.. code-block:: 

    >>> some_primes = [2, 3, 5, 7, 11, 13, 17, 19]
    >>> len(some_primes)
    8

Lists can be empty, in which case ``len`` will report that the length is 0. Notice that we write the empty list as simply ``[]``.

.. code-block:: 

    >>> len([])
    0

Additionally, the ``sum`` function takes a list of numbers and produces their total:

.. code-block:: 

    >>> sum([1, 100, 50])
    151