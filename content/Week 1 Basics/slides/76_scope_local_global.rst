Scope: local vs. global
=======================

Let's take a look at the following simple code.

.. code-block:: python

    def assign_x(num):
        x = num

    x = 10
    assign_x(8)
    print('The value of x is:', x)

The function ``assign_x(num)`` is defined to assign ``x`` with the given value ``num``. After defining the function, ``x`` is set to be 10, and ``assign_x(8)`` is called, which runs ``x=8``. Then, the last line prints the value of ``x`` to the screen. Now, one may expect that the output would show ``The value of x is: 8``. However, our actual output is

.. code-block:: 

    The value of x is: 10

What is happening here? The value of ``x`` hasn't been changed although ``print`` function was called after ``assign_x(8)``. This is because ``x`` in ``assign_x`` function was treated as a local variable, which exists only in the local scope of ``assign_x`` function. It's about time to learn what local/global scope is. 

A parameter or variable that is assigned or declared in a function is called a **local variable**, and it is said to be in the **local scope** of that function. When a function is returned, every local variable in that function is forgotten. On the contrary, a variable that is declared outside all functions is called a **global variable**, which is in the **global scope**. The global scope is created when the program begins. While there can be as many local scopes as there are functions, there is only one global scope.

Please note that a variable cannot be both local and global, even if a variable of the same name appeared in each other's scope. In the example above, when ``x=10`` is implemented, ``x`` is a global variable. However, when ``assign_x(8)`` is called, a new local variable named ``x`` is created and assigned with ``num``. Python has its own way to tell apart the global ``x`` and the local ``x``. After ``assign_x(8)`` is returned, the data of the local variable ``x`` is removed. When the last line with ``print`` function is called, ``x`` is the global one, which is why our result showed that ``the value of x is 10``. 

Now that we have figured out how local and global scopes are different, let's think about the following code. 

.. code-block:: python

    def assign_x(num):
        x = num
        print('The value of x is:', x)

    x = 10
    assign_x(8)
    print('The value of x is:', x)

This is the same as the previous example except that ``assign_x`` function also has a line to print the value of ``x``. The output is as follows.

.. code-block::

    The value of x is: 8
    The value of x is: 10

The first line shows that ``x`` is 8, because ``print`` inside the call of ``assign_x`` function deals with the local variable ``x``, the value of which is 8. The next line reads that ``x`` is 10, since it is using the global variable ``x``.