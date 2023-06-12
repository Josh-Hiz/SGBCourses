Testing Membership in Lists
===========================

We can use the ``in`` and ``not`` in to check if a particular element is present in a list or not. The format of using these operators is that you specify the element you want to check, followed by the ``in``/ ``not in`` operators, followed by the list in which you want to check.

Let's consider the same list we have used before:

.. code-block::

    >>> wages = [40.25, 51.5, 35.4, 42.34]
    >>> 35.4 in wages
    True
    >>> 38 in wages
    False
    >>> 38 not in wages
    True