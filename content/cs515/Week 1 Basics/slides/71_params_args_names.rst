Parameter names vs. argument names
==================================

Most of the time, **parameters** and variable **arguments** will have different names. For example, take a look at this code.

.. code-block:: python

    def add_numbers(num1,num2):
        return num1 + num2

    x = 1
    y = 100
    print(add_numbers(x,y))

The **arguments** are the variables ``x`` and ``y``, and the **parameters** are ``num1`` and ``num2``. It is relatively straightforward to follow that the **argument** ``x`` is passed into the **parameter** ``num1`` when ``add_numbers()`` is called, and similarly ``y`` is passed into ``num2``.