Floating Point Numbers, Redux
=============================

Most of the calculations we've seen so far have worked with *integers*, and we've referred to them as both “numbers” and “integers.” We've also run into a different kind of number --- *floating point numbers*. Floating point numbers --- *floats* for short---behave a little differently than integers, and also different than the real numbers you know from math. For example, with division, the result appears to be a decimal number up to a certain precision:

.. code-block:: python

    >>> 1/3
    0.3333333333333333
    >>> 1/10
    0.1

but if we try to do arithmetic, something odd happens:

.. code-block:: python

    >>> 1/10 + 2/10
    0.30000000000000004

Python has given us a wrong mathematical answer! 😭 Why? Python (along with many other languages) uses **floating-point numbers** for arithmetic with non-whole numbers. Floats are often a good approximation for the reals, but: 

* not every real number can be represented as a float (and not just because our computer's memory is finite)
* the order of operations on floats can matter (``0.3`` isn't the same as ``0.1 + 0.2``)

Python Floating-Point Number versus Integers
--------------------------------------------

So, what is the difference between a floating-point number and an integer? Both integers and floating-point numbers represent a type of numerical data. An **integer** is a type of data that does not have a decimal point. A **floating-point number** is a data type that is used to represent non-whole numbers.

**Is there a difference between 1 and 1.0?**

**Yes!** ``1`` is an integer value, there is **NO** decimal point, where as ``1.0`` is a floating-point number, it **HAS** a decimal point.