__name__ == "__main__"
======================

Python files by default define modules. If you write bare code---like a ``print`` in ``__init__.py`` or ``main.py`` in the previous example---it will run every time the module runs. That isn't always a good thing! Sometimes we want to define a module but *not* run the code in it. (For example, ``doctest`` and ``unittest`` can both be run as code or simply imported as modules.) We need a way to differentiate between the two situations: **do we want to load the module definitions and run the code, or do we only want to load the module definitions?**

To differentiate, Python offers the ``__name__`` facility. ``__name__`` is a global variable that tells you the name of the current module. If your code is being loaded via ``import``, then ``__name__`` will be the module name (e.g., ``algorithms.sort``). If your code is being run via ``python`` or ``python -m``, then ``__name__`` will be ``__main__``.

Here's an example: suppose we have a file ``task.py``.

.. code-block::

    # this is task.py

    print(f'Hello, my __name__ is {__name__}.') 

Here's what we get when we invoke ``task`` as the main module:

.. code-block::

    $ python task.py
    Hello, my __name__ is __main__.
    $ python -m task
    Hello, my __name__ is __main__.

And here's what happens when we ``import task`` in a Python interpreter:

.. code-block::

    $ python
    Python 3.9.7 (default, Oct 19 2021, 17:23:38) 
    [Clang 10.0.0 (clang-1000.11.45.5)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import task
    Hello, my __name__ is task.

You can `read more about __main__ in the Python docs <https://docs.python.org/3/library/__main__.html>`_.

Conditional behavior
--------------------

It's very common for a Python module to offer a bunch of definitions as well as useful "main program" behavior. We can have the program offer both by conditioning on ``__name__``, as follows:

.. code-block::

    # definitions here

    if __name__ == '__main__':
        # main program code here