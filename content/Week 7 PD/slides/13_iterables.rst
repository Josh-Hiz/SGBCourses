Iterables
=========

We've seen that lists, tuples, strings, and dictionaries can all be used in ``for`` loops. These data structures are all **iterable**. We've encountered some more esoteric iterables, too: ``range``, ``map``, and ``filter`` all return iterable objects.

Python uses a simple protocol for iterators, with two functions. To make an object iterable, it needs a ``__iter__(self)`` method that returns an **iterator**. An **iterator** must define ``__iter__ (typically just returning self)`` and ``__next__(self)``, which either returns the next value or raises ``StopIteration``.

Here's an example of an iterator that counts by odds up to 100:

.. runner::

    class Odds(object):
        def __init__(self):
            self.__v = 1

        def __iter__(self):
            return self

        def __next__(self):
            v = self.__v

            if v >= 100: raise StopIteration

            self.__v += 2
            return v

    for x in Odds():
        print(x)

Notice how ``Odds`` keeps some internal state!