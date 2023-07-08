Visualizing recursive call stacks
=================================

Recursive functions build up a stack as they work. Consider the ``sumup`` function we defined:

.. runner::

    def sumup(n):
        if n <= 0:
            return 0

        return n + sumup(n-1)

    print(sumup(10))

As ``sumup`` runs, each addition is pending on the call stack, as we wrote before:

* ``sumup(10)`` --- since ``10 > 0``, we go to the recursive case, computing...
* ``10 + sumup(9)`` --- since ``9 > 0``, we go to the recursive case, computing...
* ``10 + 9 + sumup(8)`` --- since ``8 > 0``, we go to the recursive case, computing...
* ``10 + 9 + 8 + sumup(7)`` --- since ``7 > 0``, we go to the recursive case, computing...
* ...and so on, until we have...
* ``10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + sumup(1)`` --- since ``1 > 0``, we go to the recursive case, computing...
* ``10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 + sumup(0)`` --- and it's not the case that ``0 > 0``, so sumup(0) returns 0, and we have...
* ``10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 + 0`` which is ``55``.

It's important to understand that each addition is waiting in its own stack frame. Using `PythonTutor <https://pythontutor.com/visualize.html#mode=display>`_, it's easy to see this in the progressive return values through each frame.

In order to understand, write, and debug recursive functions, you need to be able to picture the call stack in your mind. The best way to do this is to *practice*, by drawing how recursive functions are working on the board. Here's a program with an interesting recursion: it sums up all of the numbers in *arbitrarily nested lists*. Notice how it uses ``isinstance`` to decide how to work:

.. runner::

    def nested_sum(v):
        if isinstance(v, int):
            return v
        elif isinstance(v, list):
            if len(v) == 0:
                return 0
            else:
                return nested_sum(v[0]) + nested_sum(v[1:])
        else:
            raise TypeError('nested_sum expects lists (of lists of...) ints')

    print(nested_sum([1,[2,3],4,[5,[6]]]))

Try drawing the stack of this program as it executes the function call at the bottom.