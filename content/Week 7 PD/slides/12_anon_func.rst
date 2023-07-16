Anonymous function practice
===========================

Please define a function ``longest_lines`` that takes in a filename and returns all of the lines in that file of that length.

For example, if we have a file ``foo.txt``:

.. code-block::

    a
    b
    cd
    ef
    g

Running ``longest_lines('foo.txt')`` will return ``['cd', 'ef']``. Try to do it using ``map``, ``filter``, and ``lambda``.

Hint 1: you can use ``max`` on a list.

.. runner::

    print(max([1,2,3,-2,-1]))

Hint 2: if you define one function inside another, you can access the outer function's variables.

.. runner::

    def shout_it_out(l):
        to_add = "!"

        def shout(s):
            return s + to_add # using variable from shout_it_out

        return map(shout, l)

    l = shout_it_out(["this", "is", "called", "'closing'", "over", "a", "variable"])
    print(list(l))

.. challenge::
    :tester: /_static/cs515_challenges/Week7/Challenge3/test.py

    # define longest_lines