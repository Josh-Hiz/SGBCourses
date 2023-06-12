A method to our madness
=======================

So far, we've seen that we can do computation on values using **operators** like +, -, <, and ==, or with **functions** like max, min, abs, or len.

There's one other common way of working with values in Python (and many programming languages) that looks different, but is in fact quite related to functions. In Python we can write:

.. code-block:: 

    >>> s = "hello!"
    >>> s.upper()
    'HELLO!'

In this example, we say that upper is a **method**, and the syntax ``s.upper()`` is a **method call** or **use of a method**. As the name suggests, it converts the string stored in s to upper case.

Here's another example of using a method that gives the count of the string given as a parameter in the string ``s``:

.. code-block::

    >>> s.count("l")
    2
    >>> s.count("h")
    1

To use a method, we first need to have some value (also called an **object**) with some methods defined for its type. In this case, that object is a string, and strings have lots of methods defined (https://docs.python.org/3/library/stdtypes.html#string-methods). Then, we can write:

.. code-block:: 

    object.method-name(argument1, argument2, ...)

We document methods slightly differently from functions. In addition to the name and arguments, we write the type name, in this case str. For count, we'd write:

.. code-block::

    str.count(sub)

    Takes a string sub and produces the number of times the string sub appears in this string.

We'll often use phrases like "this string" to refer to whichever string we used right before the dot. So in our example above with ``s.count("l")`` , "this string" would be referring to the string "hello" stored in s, and the string we're counting would be the value of the argument sub (i.e., the string ``"l"``).

(Aside: For all our uses in CSE8A, methods and functions accomplish all the same goals. Python could have decided to implement count as a function that takes two arguments, a string called s and a string sub to count occurrences of sub in s. In fact, Python had this function in an earlier version, but removed it in Python 3. However, since methods are the only way to do certain operations in Python, we will learn and practice the syntax for method calls.)

**Summary: method calls are a lot like function calls, but we call them using an object followed by a dot and also document them differently.**