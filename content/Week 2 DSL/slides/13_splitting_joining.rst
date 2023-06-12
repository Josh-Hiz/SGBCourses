Splitting and Joining
=====================

There are functions and methods that produce lists. In general, you should expect to find lists mentioned in the documentation of many methods! One such example that will be useful for us is the ``split`` `method on strings <https://docs.python.org/3/library/stdtypes.html#str.split>`_:

``str.split(sep)``

Returns a list of strings appearing between instances of sep in the string.

.. code-block:: 

    >>> "1:2:3".split(":")
    ['1', '2', '3']
    >>> "apple banana orange".split(" ")
    ['apple', 'banana', 'orange']

We've been using the split method a lot in the exercises behind the scenes: it helps us take a bunch of input that appears on one line with spaces in between interesting parts, and then split it into the interesting parts in a list.

There's a related method called join that does the opposite of splitting:

``str.join(lst)``

Takes a list of strings and returns a string made by concatenating the elements of lst with this string in between.

.. code-block::

    >>> ":".join(["1","2","3"])
    '1:2:3'
    >>> " ".join(["apple", "banana", "orange"])
    'apple banana orange'