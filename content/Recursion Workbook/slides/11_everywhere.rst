Everywhere
==========

Define a function ``everywhere(f, v)`` that acts like ``map(f, v)``, except it explores ``v`` deeply---applies ``f`` everywhere on ``v``. That is, if ``v`` is a list you should run ``everywhere(f, ...)`` to build a new inner list.

For example:

.. code-block:: 

    >>> everywhere(lambda n: n + 1, [1, 2, [10, 20, [100]], 1000])
    [2, 3, [11, 21, [101]], 1001]

Can you do this with no ``for`` or ``while`` loops at all?

.. challenge:: 

    