Explaining what you're about
============================

The ``dir`` function just tells what exists, but the ``help`` function does much more: it shows you important information about various definitions. The ``help`` text in Python isn't automatically generated: a human wrote it all!

Python supports **comments** in code using the ``#`` sign---we've used it to prevent code from running, or to remark on what we're doing. But it also supports a different kind of comment. **Docstrings** are special strings that document definitions, like so:

.. code-block:: python

    def fact(n):
        """Returns factorial of n
        
        Returns 1 on all numbers < 2
        """
        res = 1
        while n > 1:
            res *= n
            n = n - 1
        return res

Now see what happens when we run ``help(fact)``:

Very cool! Writing docstrings takes time, but it's really helpful to explain what a function does to your teammates. Even if you're the only one working on the project... will you remember *all* the details in six months?

Note that you can look at docstrings in your code, i.e.,

.. code-block:: 

    >>> fact.__doc__
    'Computes factorial of n, an int\n    \n    Returns 1 on all numbers < 2\n    '

We recommend glancing at the `Python documentation on docstrings <https://peps.python.org/pep-0257/>`_. Docstrings can occur in modules (at the top), in classes (right after the ``class`` line), in methods (after the ``def`` line), or in functions (after the def line). Unfortunately, it's not possible to docstring a field or a constant (as of Python 3.9.6).