Passing Arguments to Functions
==============================

When you call a function, like ``print()`` , ``len()``, or one you define yourself, you pass in values between the parenthesis, which are called **arguments**. **Arguments** can be any **object**, such as a **list**, **integer**, or **string**. For example, when we call ``len()`` on a **list**, the **list** is the argument. For example:

.. code-block:: python

    a = [1,2,3]
    len(a)

In this case, when we make the function call ``len(a)``, the **list** a is the **argument** to the function ``len()``.

Some functions take **multiple arguments**. For example, the ``range()`` function. When we make a call like ``range(-10,10)``, we are using two **arguments**, the first of which specifies a starting integer, and the second of which specifies the stopping integer. Arguments are separated by a ``,`` (comma).

You may also recall that ``input() `` can may or may not take an **argument** which specifies prompt. For example, ``input()`` will just read input, but ``input('What is your name? ')`` will show ``What is your name?``  before reading input. Many functions have such **optional arguments**, which have a default value if not specified. We don't have the knowledge yet to write our own, but be aware that they exist. In the case of **input()**, if the prompt isn't specified, it will default to ``''``, the empty string. 

Some functions can even be called with **no arguments**. For example, calling ``print()`` with **no arguments** (nothing between the parenthesis) will result in a new line being printed and nothing else. We can create our own function that requires no **arguments** quite easily. For example, here is a function that requires **no arguments** and simply returns 1.

.. code-block:: python

    def return_one():
        return 1

Arguments can be a little perplexing, but they add a lot of power and flexibility to our function calls.