Boolean Expressions Using Variables
===================================

Boolean values can be stored in variables just like strings and numbers. 

.. code-block:: python

    >>> x = 10
    >>> is_greater_than_10 = (x > 10)
    >>> is_greater_than_10
    False

A common misconception is that entire expressions get stored, rather than the boolean value (``True`` or ``False``).

.. code-block:: python

    >>> w = 22
    >>> is_equal_to_22 = (w == 22)
    >>> is_equal_to_22
    True
    >>> w = 15
    >>> is_equal_to_22
    True

Comparators work on most types.

.. code-block:: python

    >>> name = "Michelle"
    >>> form_submission_name = "Michael"
    >>> is_same_person = (name == form_submission_name)
    >>> is_same_person
    False
    