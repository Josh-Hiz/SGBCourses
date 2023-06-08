There and Back Again: Converting Between Integers and Floats
============================================================

What happens if we want to convert a value represented as a floating-point number to be represented as an integer? We already know that to change a value to the data type integer we need to use the function ``int()``. Integers are always whole numbers with no decimal value, you can think of it as if anything that would have come after the decimal point is simply cut off. How can we convert an integer value to a floating-point number? We can use the function ``float()``.

Here are some examples of both:

**Examples using int()**
------------------------

.. code-block:: python

        >>> int(2.0)
        2
        >>> int(2.5)
        2
        >>> int(2.7)
        2

Notice that ``int(2.7)`` does **NOT** return ``3``---it returns ``2``. This is because everything after the decimal place is simply cut off, or *truncated*. 

**Examples using float()**
--------------------------

.. code-block:: python

        >>> float(2)
        2.0
        >>> float(5)
        5.0
        >>> float(11)
        11.0

Notice that ``int(2.7)`` does **NOT** return ``3``---it returns ``2``. This is because everything after the decimal place is simply cut off, or *truncated*. 

**Note:** Operations that convert from one datatype to another are called **casting operations**. Casting often comes with a **loss of information** as when going from floats to integers and losing the fractional part of the number.



 