Introduction to Booleans
========================

Booleans
--------

As we stated in *1.1 Basics of Numbers and Variables*, programs do their work with data. Here we will be introducing a new type of data: **Booleans**. Booleans are a type of data that is essentially yes/no (whether a box is checked). A boolean is either ``True`` or ``False``, there are only two possible values. They're named after `George Boole <https://en.wikipedia.org/wiki/George_Boole>`_.

At a Python prompt (after the ``>>>`` in IDLE or at a terminal after running ``python``), try typing a boolean and pressing enter. Here's what you should expect to see:

.. code-block:: python

    >>> True
    True
    >>> False
    False

Boolean Expressions
===================

**Boolean expressions** are expressions that evaluate to a boolean value, either ``True`` or ``False``. There are many operators that allow us to evaluate boolean expressions, in two broad categories: comparisons and logical operators.

Comparisons 1: Inequalities
---------------------------

The first relational operators we'll meet are the inequalities, written ``<`` (for less than), ``<=`` (for less-than-or-equal-to, i.e., ≤), ``>`` (for greater than) and ``>=`` (for greater-than-or-equal-to, i.e., ≥). These are all written in the conventional way and with the conventional numerical meaning. They return ``True`` when the inequality holds and ``False`` when it doesn't.

.. code-block:: python

    >>> 8 > 7
    True
    >>> 7 > 8
    False
    >>> 8 >= 8
    True
    >>> 10 <= 17
    True

Comparisons 2: Equalities
-------------------------

To test for equality, we use ``==``. We've already encountered the ``=`` sign elsewhere: it's used for variable assignment. Confusing the two is an *extremely* common mistake, even for experienced programmers.

.. code-block:: python

    >>> 10 == 10
    True
    >>> 10 == 9
    False
    >>> x = 10   # THIS IS AN ASSIGNMENT, NOT A COMPARISON!!!!
    >>> x == 9
    False
    >>> x == 10
    True

``True`` if the values are equal, ``False`` otherwise

.. code-block:: python

    >>> 10 == 10
    True
    >>> 10 == 9
    False
    >>> x = 10
    >>> x == 9
    False
    >>> x == 10
    True

Comparisons 3: Anti-Equalities
------------------------------

The ``!=`` operator means "not equal to", i.e., the ≠ operator from mathematics. It returns 

The ``!=`` operator means "not equal to", i.e., the ≠ operator from mathematics. It returns ``True`` if the values are *not* equal, and ``False`` otherwise.

.. code-block:: python

    >>> 10 != 10
    False
    >>> 10 != 9
    True

Logical Operators
-----------------
There are three common logical operators in programming: ``and`` a/k/a conjunction, ``or`` a/k/a disjunction, and ``not`` a/k/a negation.

The ``and`` operator returns ``True`` if *both* of its arguments are ``True``.

.. code-block:: python

    >>> True and True
    True
    >>> False and True
    False
    >>> True and False
    False
    >>> False and False
    False

The ``or`` operator returns ``True`` if either *or* both expressions evaluate to ``True``, and returns ``False`` otherwise.

.. code-block:: python

    >>> True or True
    True
    >>> True or False
    True
    >>> False or True
    True
    >>> False or False
    False

Finally, the ``not`` operator invers its Boolean argument.

.. code-block:: python

    >>> not True
    False
    >>> not False
    True
