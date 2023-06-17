Sets
====

One final useful structure in Python is the **set**. While a dictionary maps (unique) keys to values, a set stores a collection of unique elements. Here's an example:

.. runner::

    s = set()
    s.add(1)
    s.add(2)
    s.add('hi')
    print(s)
    print('hi' in s)
    print(len(s))
    s.add(2)
    print(len(s)) # why no change?
    s.remove(2)
    print(len(s))
    print(s)

Like it does for lists and dicts, Python supports a special notation for sets: curly braces. You might be confused... don't dictionaries use those, too? They do, and it can be tricky!

.. runner::

    s = {1, 2, 'hi'}
    print(type(s))
    print(s)

    s = {True} # just one, a 'singleton'
    print(type(s))

    x = {}
    print(type(x))

If ``{}`` defaults to a dictionary, how then do you write the empty set? Easy: you use the ``set()`` constructor:

.. runner::

    s = set()
    print(type(s), s)
    s.add(1)
    s.add(2)
    s.add(1)
    print(len(s), s)

    # you can use the constructor to make a set!
    l = [1,2,3,4,5,1,2,3,4,5,0]
    s = set(l)
    print(s)

Make sure to run ``help(set)`` to learn more about ``set`` operations in Python.