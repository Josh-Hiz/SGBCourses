String Comparison
=================

In python, we can compare strings using the ``==`` and ``!=`` operators. Both of these operators can be used to compare two strings and will evaluate to a Boolean. The ``==`` operator will evaluate to ``True`` if the two strings are the same and ``False`` if they are different.

.. code-block:: python

    >>> "apple" == "apple"
    True
    >>> "apple" == "banana"
    False

The ``!=`` operator will evaluate to ``True`` if the two strings are different and ``False`` if the two strings are the same.

.. code-block:: python

    >>> "apple" != "apple"
    False
    >>> "apple" != "banana"
    True

Note that in Python, two strings are considered to be equal only if all characters in the two strings are equal including their case (i.e., lower or upper case). Therefore, "apple" is not the same as "Apple" and similarly the two strings "banana" and "BANANA" are not equal.

.. code-block:: python

    >>> "apple" == "Apple"
    False
    >>> "banana" == "BANANA"
    False