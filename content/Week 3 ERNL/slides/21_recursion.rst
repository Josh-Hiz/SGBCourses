Recursion: functions that call themselves
=========================================

**Recursion** is when things refer back to themselves; we'll be studying recursive functions. That is, we're going to learn about functions that call themselves.

Here's a simple recursive function that counts up to ten:

.. runner::

    def countup(n):
        # BASE CASE
        if n > 10:
            return
        
        # RECURSIVE CASE
        print(n)
        countup(n+1)

    countup(1)

How does this function work? Running it in `PythonTutor <https://pythontutor.com/visualize.html#mode=display>`_ is a helpful visualization. Each time **countup** is called, it checks to see if it's hit its limit, ``n > 10``. If it has, it just returns. If it's not yet at the limit, ``countup`` prints out ``n`` and *calls itself* with ``n`` one greater.

Here's another example, where we'll count down to 0, summing numbers as we go.

.. runner::

    def sumup(n):
        if n <= 0:
            return 0

        return n + sumup(n-1)

    print(sumup(10))

Again, `PythonTutor <https://pythontutor.com/visualize.html#mode=display>`_ is a great help. Here's what happens:

* ``sumup(10)`` --- since ``10 > 0``, we go to the recursive case, computing...
* ``10 + sumup(9)`` --- since ``9 > 0``, we go to the recursive case, computing...
* ``10 + 9 + sumup(8)`` --- since ``8 > 0``, we go to the recursive case, computing...
* ``10 + 9 + 8 + sumup(7)`` --- since ``7 > 0``, we go to the recursive case, computing...
* ...and so on, until we have...
* ``10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + sumup(1)`` --- since ``1 > 0``, we go to the recursive case, computing...
* ``10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 + sumup(0)`` --- and it's not the case that ``0 > 0``, so ``sumup(0)`` returns ``0``, and we have...
* ``10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 + 0`` which is ``55``.

In recursive functions, we say something is a **base case** if it doesn't make a recursive call, and we say it's a **recursive case** otherwise. In the case of ``countup``, ``if n > 10: return`` is a base case. For ``sumup``, the base case is if ``n <= 0: return 0``.