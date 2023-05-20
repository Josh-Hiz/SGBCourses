Adding, Subtracting, Multiplying and Dividing with Floating-Point Numbers
=========================================================================

If you are calculating a numerical value and only using the data type floating-point, your answer will also be a floating-point number. If you are using both integers and floating-points numbers, the result will be of the data type floating-point.

.. code-block:: python

    >>> 5 + 5.0
    10.0
    >>> 5 - 5.0
    0.0
    >>> 5 * 5.0
    25.0
    >>> 5 / 5.0
    1.0

This is true for integers, except in the case of using the ``/`` operator for division, this will always return a floating point number so that your answer will not lose precision, otherwise an operation such as ``5/2`` would evaluate to ``2``.

.. code-block:: python

    >>> 5 + 5
    10
    >>> 5 - 5
    0
    >>> 5 * 5
    25
    >>> 5 / 5
    1.0
    >>> 5 / 2
    2.5

Notice how the example of ``5/5`` evaluates to ``1.0`` and ``5/2`` evaluates to ``2.5``, both floating-point numbers. 