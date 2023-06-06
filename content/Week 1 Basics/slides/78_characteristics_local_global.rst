Characteristics of local and global variables
=============================================

Local and global scopes have different characteristics. Your code in the global scope cannot access any local variable. Actually, a local variable can be used only in the local scope that it belongs to, and the local variable cannot be accessed by other local scopes. However, your code inside functions can access global variables, because they are global. 😁 Further, as we've already seen, the same name can be used for variables from different scopes. Python can tell apart!

The following code shows that global variables can be used in a function

.. runner::

    def local():
        print('The value of x is:', x)

    x = 10
    local()

Here is the output:

.. code-block::

    The value of x is: 10

Since ``x`` is a global variable, the ``local`` function can access ``x`` and prints out its value. Since the ``local`` function does not have a local variable named ``x``, so it automatically looks for a global variable ``x``.

However, the following code does not work.

.. runner::

    def local():
        x = 10
    local()
    print('The value of x is:', x)

We get an error: 

.. code-block:: 

    NameError: name 'x' is not defined

This is because ``x`` defined in the local scope of the ``local`` function cannot be used in the global scope.

Also, a local variable cannot be used in another local scope as seen in the following example.

.. runner::

    def local():
        x = 10

    def local2():
        print(x)

    local()
    local2()

This example has an error as well, because ``x`` was assigned in the ``local`` function, and the ``local2`` function cannot see the value of ``x``.

Finally, function calls can't see locals beyond their stack frame---local variables really only live in the scope of their function call.

.. runner::

    def local():
        x = 10
        local2()

    def local2():
        print(x)

    local()