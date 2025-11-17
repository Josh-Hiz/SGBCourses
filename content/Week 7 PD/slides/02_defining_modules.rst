Defining your own modules
=========================

Every Python file defines a **module**. We've seen modules already by way of the import statement, which tells Python that we'd like to use someone else's code. There's a lot to learn about modules--- `check out the Python documentation <https://docs.python.org/3/tutorial/modules.html>`_. We'll learn two things:

* how to define your own modules
* where Python looks for modules

Defining a module is as simple as defining a file---if you create one file ``foo.py``, then you can run ``import foo`` in **another file** to load in foo's definitions.

So, if you have a file ``util.py``:

.. code-block::

    # this is util.py

    def fact(n):
        res = 1
        while n >= 2:
            res = res * n
            n = n - 1
    return res

If you create a file ``main.py`` in the same directory, you can reference ``util`` in a few ways. You can use ``import`` and then reference ``util``'s definitions using the ``.`` operator:

.. code-block::

    # this is main.py (version 1)
    import util

    print(util.fact(5))

    our_fact = util.fact # you can bind modules' definitions locally

    print(our_fact(5))

Or you can directly import a definition from ``foo``:

.. code-block::

    # this is main.py (version 2)
    from util import fact

    print(fact(5))

Module resolution
-----------------

We saw that a file named ``util.py`` resolved to a module ``util``. But we've used other modules---like ``math`` or ``random`` that don't have files in the same directory. What's going on?

Python resolves modules in one of three ways:

* Relative to the directory of the initial Python script (or the directory where ``python`` was run).
* Relative to colon-separated directories in the ``PYTHONPATH`` environment variable.
* Relative to the global "site packages" and user site packages directories, which is globally specified for a given installation.

(There are also some sneaky, built-in packages that are part of Python itself.)

You can `read more about these details in the Python documentation <https://docs.python.org/3/tutorial/modules.html#the-module-search-path>`_.