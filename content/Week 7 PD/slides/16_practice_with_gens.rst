Practice with generators
========================

Write a generator function ``odds_up_to(n)`` that uses yield to generate odds from ``1`` up to ``n``, inclusive (if ``n`` is odd).

Here's a sample interaction:

.. code-block:: 

    >>> for x in odds_up_to(5): print(x)
    ...
    1
    3
    5
    >>> for x in odds_up_to(1): print(x)
    ...
    1
    >>> for x in odds_up_to(2): print(x)
    ...
    1

.. challenge::

    