Variable arity with \*args
==========================

A function's **arity** is the number of arguments it expects. For example ``math.sqrt`` has an arity of 1; the function ``binary_search`` has an arity of 2. The function ``print``... can take 0, 1, or however many arguments. We say that print has **variable arity**.

Python lets you define variable arity by marking a special argument with a ``*``; conventionally, this argument is called ``args``. Here's an example:

.. runner::

    def f(x, y, *args):
        print(f'x is {x}')
        print(f'y is {y}')
        print(f'*args is {args}')

    f(0, 1)
    f(0, 1, 2)
    f(0, 1, 2, 3)
    f(0)

Notice a few things:

* Every declared **positional argument** must be present (note the final exception).
* The ``*args`` parameter receives any "excess" paramters.
* The ``*args ``parameter is a tuple.

In principle, you could *just* use ``*args``, never declaring positional parameters. That would be a terrible idea: positional argument document clearly what a function *needs*, making it an error to leave them out. Parsing out coherent arguments from ``*args`` is tedious and error-prone, too.

Supplying \*args
----------------

It's also possible to call a function using explicit variable arity; mark the argument list with a ``*``. Here's an example:

.. runner::

    def f(x, y, *args):
        print(f'x is {x}')
        print(f'y is {y}')
        print(f'*args is {args}')

    f(*(0,1,2))
    f(0,1,*[2,3,4])
    f(0, *[1,2])

    f(*"abc")
    f(*[0])

Using ``*args`` when calling says, "``args`` is iterable, and you should use is for the rest of the arguments for this function". The first three examples show how positional variables interact; the fourth example shows that any iterable works---even a string. The last example shows that we get an error when ``*args`` doesn't give us enough arguments.