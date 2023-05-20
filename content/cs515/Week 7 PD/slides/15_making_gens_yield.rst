Making generators with the yield keyword
========================================

Writing iterators is hard. Python makes it easier for you by making it easy to turn a function into a special kind of iterator, called a **generator**. In principle generators or simple, though there are many nuances that deserve careful attention --- `read the docs <https://docs.python.org/3.9/reference/expressions.html#yieldexpr>`_!

Here's an example generator for the Collatz conjecture:

.. exec_code::

    def collatz(n):
        assert isinstance(n, int), "n must be an int"
        assert n >= 1, "n must be positive"

        # initial value
        yield n

        while n != 1:
            if n % 2 == 0: n = n // 2
            else: n = n * 3 + 1

            yield n

    print(collatz(5))
    for x in collatz(5): print(x)

When you use the ``yield`` keyword in a function, Python compiles the function specially so that it will be an iterator. The ``__next__`` method it generates runs your function until the next ``yield``, which provides the next value in the iteration.

There are subtle rules for how ``yield`` and ``return`` and exceptions interact, particularly because a generator's return gets translated to a ``StopIteration`` exception. If you can, it's best to avoid mixing ``yield`` and ``return``.