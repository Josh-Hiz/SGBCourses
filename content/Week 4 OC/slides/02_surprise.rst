Surprise: we've been using objects!
===================================

Python uses OOP notations extensively, and we've *already* been programming with objects. Python lists, strings, and dictionaries are all objects. Each instance of ``ValueError`` and all of the other ``Errors`` we've met.

Method calls take the form ``o.m(arg1)``, where you call the method ``m`` on the object ``o`` with the argument ``arg1``. A method is a function that runs "on" an object. That is, the code for ``m`` will be able to work on both the argument ``arg1`` and the **receiver** ``o``. We've seen this notation for, e.g., ``"hello there".split()`` or ``l = []; l.append(5)``. 

We haven't seen fields yet, but they've been there in the background. For example, here's an example with a ``ValueError``:

.. runner:: 

    v = ValueError('alas, poor Yorick')
    print(v.args)

Here ``v.args`` is us getting the **field** or **member** ``args`` from the object ``v``, whose class is ``ValueError``.

Notice that accessing a field is just like calling a method---only you leave off the parentheses. The ``object.thing`` dot-notation is a nice one: it expresses the idea that ``thing`` "belongs" to ``object``, whether ``thing`` is a method or a field.

We've also seen the dot-notation for working with modules, i.e., ``math.sqrt(16)``. In Python, modules *are* objects, but the functions in a module *are not* methods.