The Collatz conjecture
======================

The `Collatz conjecture <https://en.wikipedia.org/wiki/Collatz_conjecture>`_ suggests that if you pick any positive integer, iterating the following process will always arrive at 0:

1. If your number is even, halve it.
2. If your number is odd, triple it and add one.

Define a python iterator ``Collatz(n)`` whose constructor takes a starting number and iterates the Collatz process until 1 is reached.

Here's an example interaction:

    >>> Collatz(5)
    <__main__.Collatz object at 0x7faf747aad00>
    >>> for x in Collatz(5): print x
        File "<stdin>", line 1
            for x in Collatz(5): print x
                                       ^
    SyntaxError: invalid syntax
    >>> 
    >>> for x in Collatz(5): print(x)
    ... 
    5
    16
    8
    4
    2
    1
    >>> Collatz(0)
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "/home/task.py", line 4, in __init__
            assert n >= 1, "n must be positive"
    AssertionError: n must be positive
    >>> Collatz(1.3)
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "/home/task.py", line 3, in __init__
            assert isinstance(n, int), "n must be an int"
    AssertionError: n must be an int

.. challenge::

    # define Collatz