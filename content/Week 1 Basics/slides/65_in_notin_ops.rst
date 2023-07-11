Using \`in` and \`not in` Operators
===================================

You can determine whether a character is or isn’t in a string with the ``in`` and ``not in`` operators. Like other operators, ``in`` and ``not in`` are used in expressions and connect two values: a character to look for in a string and the string where it may be found. These expressions will evaluate to a Boolean value.

.. code-block:: python

    >>> "a" in "apple"
    True
    >>> 'b' in 'apple'
    False

Since the character ``"a"`` is in ``"apple"``, it evaluated to ``True``. Likewise, since ``'b'`` is not in ``'apple'``, it evaluated to ``False``.

.. code-block:: python

    >>> 'a' not in "apple"
    False
    >>> "b" not in 'apple'
    True

The ``not in`` operator is the opposite of the ``in`` operator. Notice that the results are the opposite from ``in``. Since the character ``'a'`` is in ``"apple"``, it evaluated to ``False``. Since ``"b"`` is not in ``'apple'`` it evaluated to ``True``.

