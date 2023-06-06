Part 2: Using Functions
=======================

There are many more kinds of computation we might want to perform beyond arithmetic. Python and many other programming languages give us lots of functionality through **functions**. Python defines a few functions for working with numbers that are **built-in**. Here's what it looks like to call the function max:

.. code-block:: python

        >>> max(4,5)
        5

We say that max *takes 2 numbers and produces a number*. We could describe or **document** the function max by saying:

.. code-block:: python

        max(n,m)

``max`` takes two numbers, ``n`` and ``m``, and produces the larger one.

In the example, we'd call 4 and 5 the **arguments** of max, and the produced value 5 the **return value** of that function call. The syntax max(4, 5) is a **function call** or a **use of a function**. A function call is written as:

* the function's name (in this case, ``max``)
* followed by arguments separated by commas in parenthesis (in this case, ``(4,5)``)

If we were reading the function call out loud, we might pronounce it in a few ways. For example, we might say “max of 4 and 5” or “max applied to 4 and 5” or “call max with 4 and 5.” It's important to have ways to pronounce code, because often we'll read out fragments of code to draw attention to something, or you will want to dictate code to your pair programming partner when they are using the keyboard.

Here are some other examples of function calls:

.. code-block:: python

        >>> abs(-3)
        3
        >>> abs(3)
        3
        >>> min(1,4)
        1
        >>> min(-3,7)
        -3