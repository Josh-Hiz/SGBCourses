Parameters vs. arguments
========================

**Parameters** and **arguments** are very closely related concepts, and you may hear the terms being used interchangeably. It is important to understand the difference to gain a full understanding of how function calls work, however. By definition, a **parameter** is a variable that an **argument** is stored in when a function is called. In other words, when you **call** a function, you pass in an **argument** which is stored in the **parameter** that was outlined when the function was **defined**. Let's get a better understanding of this concept through an example.

.. code-block:: python

    def return_plus_one(param):
        return (param+1)

This is a very simple function which returns its parameter plus 1. In any function definition, the **parameters** are defined in the first line, between the parenthesis after the function name. In this case, ``param`` is the **parameter**. Now, let's say we call this function.

.. code-block:: python

    a = 5
    return_plus_one(a)

When we call the function ``return_plus_one()`` , we use the variable ``a`` as the **argument**. An **argument** can be any **object**, which includes (but isn't limited to) an **int**, **float**, **string**, **list**, or **boolean**. Anything that can be stored in a variable can be used as an **argument**.

.. code-block:: python

    def print_and_return(param):
        print(param)
        return

In ``print_and_return()``, ``param`` is, of course, a **parameter** for the function ``print_and_return()``. However, ``param`` is also an **argument** for the ``print()`` function call within ``print_and_return()``. Though it may get a little confusing, it is important to separate what is **inside** a function call from what is **outside** of the function call, as will be illustrated in this lesson.

In class, we called a parameters **formal arguments** and we called arguments **actual arguments**.

