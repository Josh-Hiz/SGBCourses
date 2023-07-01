Printing objects out
====================

We've been able to define a few simple counter objects, along with some nice methods for working with them. But they're not very easy to debug---when you print them out, you get some weird internal gibberish.

.. code-block:: 

    >>> c = Counter()
    >>> c
    <__main__.Counter object at 0x10a48a520>
    >>> print(c)
    <__main__.Counter object at 0x10a48a520>

Not very friendly! You'll remember that other classes behave more nicely:

.. code-block:: 

    >>> v = ValueError('hi there')
    >>> v
    ValueError('hi there')
    >>> print(v)
    hi there

Python has *many* `special methods <https://docs.python.org/3.10/reference/datamodel.html#special-method-names>`_ you can define to help your objects behave the way you like. We'll learn two of them today: ``__str__`` and ``__repr__``.

Rendering nicely with ``__str__``
---------------------------------

You can control how objects are converted to strings for, e.g., printing, by defining a special method ``__str__``. It works like this:

.. runner:: 

    class Ugly(object):
        pass

    class Pretty(object):
        def __str__(self):
            return 'oh so beautiful'

    print(Ugly())
    print(Pretty())

So, we might define our counter as:

.. runner:: 

    class Counter(object):
        def __init__(self):
            self.__value = 0

        def tick(self):
            self.__value = self.__value + 1

        def value(self):
            return self.__value

        def __str__(self):
            return str(self.__value)

    c = Counter()
    c.tick()
    print(c)
    s = str(c)
    print(s)

The ``__str__`` method is very useful---it makes it easy to display the objects you're working with, and it defines how the ``str`` function will operate on your objects. It's not all roses, though: if we fire up the Python REPL to play with things, we see that the situation is still not so good.

.. code-block:: 

    >>> c = Counter()
    >>> c
    <__main__.Counter object at 0x10a6eb670>

Rendering programmatically with ``__repr__``
--------------------------------------------

The Python REPL doesn't use ``__str__`` to give a nice rendering---it uses the ``repr`` function to show the *representation* of your input, i.e., something you could copy/paste in to code. Here's an example:

.. code-block:: 

    >>> class Empty(object):
    ...   def __repr__(self):
    ...     return 'Empty()'
    ...
    >>> Empty()
    Empty()

It is standard for the ``__repr__`` definition to return what looks like call to a constructor. We've already seen this behavior with, e.g., ``ValueError``. So we could define something like the following for ``Counter``:

.. runner::

    class Counter(object):
        def __init__(self):
            self.__value = 0

        def tick(self):
            self.__value = self.__value + 1

        def value(self):
            return self.__value

        def __str__(self):
            return str(self.__value)

        def __repr__(self):
            return f'Counter({self.__value})'

    c = Counter()
    c.tick()
    print(repr(c))

If we wanted, we could update the constructor to take that format, i.e., have ``Counter(1)`` be a counter that starts at 1. Then copy/pasting would get you a new counter at the same count (though with different counting state than the one you copy/pasted, of course!). Later on in the course, we'll learn how to define flexible constructors, i.e., making it so that you can write ``Counter()`` to start at 0 and ``Counter(1)`` or ``Counter(5)`` or even ``Counter(0)`` to specify the starting point.
