Updating global variables from inside a function
================================================

The following code is written so that ``increase_x`` function can increase the value of ``x`` by 1.

.. code-block:: python

    def increase_x():
    x = x + 1
    print('The value of x is', x)

    x = 10
    increase_x()

However, this results in 

.. code-block:: python

    UnboundLocalError: local variable 'x' referenced before assignment

Although we could access a global variable from the local scope, we need an additional statement in order to modify a global variable from code in a local scope. 

With the example above, you can indicate that ``x`` in ``increase_x`` function is the global variable ``x`` by including the global statement ``global x``. A ``global`` statement is typically used at the top of a function, by writing ``global`` followed with the name of the variable, as seen in the following. 

.. py-config::

    splashscreen:
        autoclose: true

.. py-repl::
    :output: replOutput

    def increase_x():
        global x
        x = x + 1
        print('The value of x is', x)

    x = 10
    increase_x()

.. raw:: html

    <div id="replOutput"></div>

.. py-terminal::


Once a ``global`` statement is declared, it holds for the entire current code block in the local scope. Now, we have the desired result as follows.

.. code-block:: 

    The value of x is 11

In general, you should be careful when updating global state. The more global state you have, the harder your programs are to predict and debug.