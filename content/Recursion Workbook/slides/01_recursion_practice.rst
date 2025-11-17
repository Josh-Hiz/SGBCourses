Recursion Practice
==================

The following ten problems are for recursion practice. It's not for credit. There are no autograders---but we've provided solutions that include doctests.

To get the most out of this workbook, you should try to solve each problem on your own before looking at solutions. If you get it right---awesome! If not, hide the solution, take a 15min break, and try to solve it again. Once you understand the solution, move on to the next problem.

Recursion tips
--------------

The recursions here are all on lists. As a general rule, recursion on a list ``l`` will have four critical parts:

1. A base case, where you look at the list and can just say the answer. This might be when the list is empty  (``len(l) == 0``) or when it's a singleton (``len(l) == 1``), but there could be others.
2. Something that processes the first element of the list, ``l[0]``.
3. Something that processes the rest of the list, ``l[1:]``.
4. Something that combines the results of steps (2) and (3).

None of the problems here have any need for globals whatsoever. If you're using a global here, you're doing it wrong.