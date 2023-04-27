Part 4: Mixing Type is (Sometimes) an Error
===========================================

Python does **not** allow us to **add strings and numbers together**, only pairs of numbers or pairs of strings:

.. code-block::

        >>> "abc" + 123
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        TypeError: can only concatenate str (not "int") to str
        >>> 123 + "abc"
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        TypeError: unsupported operand type(s) for +: 'int' and 'str'

Read these error messages carefully. They use a fair amount of vocabulary we've introduced, like **concatenate**, **operand**, and **type**. Python refers to the type of integers as int and the type of strings as str in its error messages.

Similarly, you cannot use the **string replication operator** with both the operands as strings.

.. code-block::

        >>> 'CS ' * '515-A'
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        TypeError: can't multiply sequence by non-int of type 'str'

        The above error message says that we cannot multiply a string (which is a sequence of characters) by a string (which is not an integer).


Functions with Numbers and Strings
==================================

There are also some useful functions that work with integers and strings. For example, the function ``int``:

``int(s)``

Takes a string ``s`` made up of numeric characters and produces an integer. Reports an error if ``s`` is not a string made up of digits.

For example:

.. code-block::

        >>> int("123")
        123
        >>> int("this is just text")
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        ValueError: invalid literal for int() with base 10: 'this is just text'

You may expect that there'd be a related function that takes an integer and turns it into a string, and you'd be right! The function ``str`` does this:

``str(v)``

Takes a value ``v`` and produces its string representation.

For example:

.. code-block::

        >>> str(123)
        '123'

Note that 123 and '123' are not the same value! The first is an **integer** and can be used in arithmetic, and the second is a **string** and can only be used in string operations. For example:

.. code-block::

        >>> "abc" + str(123)
        'abc123'
        >>> "abc" + 123
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        TypeError: can only concatenate str (not "int") to str