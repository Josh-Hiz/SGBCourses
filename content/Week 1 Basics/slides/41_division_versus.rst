Division: / versus //
=====================

If there is a situation where you want to divide two numbers and you do not want anything after the decimal place, you can use ``//`` instead of ``/``. ``//`` will truncate the resulting answer, removing anything after the decimal place. 

.. code-block:: python

    >>> 5 // 2
    2
    >>> 5 // 2.0
    2.0
    >>> 5.0 // 2
    2.0
    >>> 5.0 // 2.0
    2.0
    >>> 5 // 2.0
    2.0

Looking at the last two results, note that ``//`` is still subject to promotion: if either of ``//``'s operands is a float, the result will be a float.