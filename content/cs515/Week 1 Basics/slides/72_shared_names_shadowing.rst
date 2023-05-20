Shared names and shadowing
==========================

Things can get much more tricky when we start naming our **parameters** and **arguments** the same names. Let's modify our earlier example, making it slightly more confusing.

.. code-block:: python

    def add_numbers(num1,num2):
        return num1 + num2

    num1 = 1
    num2 = 100
    print(add_numbers(num1,num2))

Though it's a lot harder to look at, this function call works exactly the same as the function call from the previous step. Only in this case, our **arguments** are named identically to our **parameters**. So, our **argument** ``num1`` (which used to be named ``x``) is passed into our **parameter** ``num1``. Similarly, our **argument** ``num2`` (which used to be named ``y``) is passed into our **parameter** ``num2``. Note that the **argument** ``num1`` is not the same variable as the **parameter** ``num1``! The following example illustrate why that is important.

.. code-block:: python

    num1 = 5
    num2 = 50
    print(add_numbers(num2,num1))

In this case, which is even harder to look at, the function call still works exactly the same as above and in the previous step. It is more important than ever to keep **arguments** and **parameters** separate, however. This time, our **argument** ``num2`` is passed into our **parameter** ``num1``, and our **argument** ``num1`` is passed into our **parameter** ``num2``.

This is intentionally confusing to highlight the difference between the variables **outside** of a function call and **inside** of a function call. In practical coding, you should avoid using the same **parameter** and **argument** names to prevent confusion.