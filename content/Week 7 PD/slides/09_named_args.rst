Named arguments with defaults with keyword arguments and \**kw
==============================================================

Python supports **named keyword arguments**. For example, the ``list.sort`` method takes an optional ``key`` argument, specifying how to perform the sort. Here's an example:

.. runner::

    l = [{'id': 100, 'name': 'Michael'},
         {'id': 73, 'name': 'Wen-Ding'},
         {'id': 112, 'name': 'Anvay'}]

    def get_id(r): return r['id']
    def get_name(r): return r['name']

    print(f'The original list is:\n\t{l}')
    l.sort(key=get_id)
    print(f'Sorted by id the list is:\n\t{l}')
    l.sort(key=get_name)
    print(f'Sorted by name the list is:\n\t{l}')

The syntax for calling a function with keywords is to write ``f(arg1, arg2, ..., argn, kw1=val1, k2=val2, ...)``.

Defining keyword arguments
--------------------------

To define a function that takes keyword arguments, you write ``def f(arg1, ..., argn, kw1=val1, ...)``. Here's an example to play with:

.. runner::

    def f(kw1=None, kw2=None):
        print(f'kw1 {kw1} kw2 {kw2}')

Here's an example interaction:

.. code-block::

    >>> f()
    kw1 None kw2 None
    >>> f(kw2=True)
    kw1 None kw2 True
    >>> f(kw1=True)
    kw1 True kw2 None
    >>> f(1)
    kw1 1 kw2 None
    >>> f(1, 2)
    kw1 1 kw2 2
    >>> f(1,kw2=2)
    kw1 1 kw2 2
    >>> f(1,kw1=2)
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    TypeError: f() got multiple values for argument 'kw1'
    >>> f(kw2=True, 2)
        File "<stdin>", line 1
            f(kw2=True, 2)
                        ^
    SyntaxError: positional argument follows keyword argument

The first example shows that keyword arguments take their default values. The second and third examples show that you can specify only one keyword argument, and the others will take their defaults. The fourth and fifth examples show that keyword arguments can be treated as positional arguments: when we write ``f(1)``, Python sees that there are no declared positional arguments, so it starts filling in the keywords from left to right. The sixth example shows that you can mix the two, but the seventh shows that you can't write positional and keyword arguments for the same keyword. Finally, the eighth example shows that you can't give positional arguments after keyword arguments.

Arbitrary keyword arguments with \**kw
--------------------------------------

Just as ``*args`` lets you define variable arity, the ``**kw`` form lets you capture *all* keyword arguments. Like ``*args``, you can use the ``**`` form both when defining and when calling a function. Here's an example definition:

.. runner::

    def g(kw1=None, **kws):
        print(f'{kw1} and {kws}')

And here's an example interaction:

.. code-block::

    g()
    None and {}
    >>> g(kw1=True)
    True and {}
    >>> g(kw2=False)
    None and {'kw2': False}
    >>> g(**{'a': 3, 'b': 4, 'kw1': 5})
    5 and {'a': 3, 'b': 4}
    >>> g(kw1=1, **{'kw1': 2})
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    TypeError: __main__.g() got multiple values for keyword argument 'kw1'

We've defined ``g`` with both an explicit keyword argument as well as ``**kw``. In general, that's a terrible idea! You should *either* use ``**kw`` or explicit keyword arguments, but probably not both.

Dangerous defaults
------------------

The default value you provide for a keyword is computed once. Here's an example of how it can go wrong:

.. runner::

    def rev(l, acc=[]):
        for x in l:
            acc.insert(0, x)
            
        return acc

    print(rev([1,2,3]))
    print(rev(list("abc")))

What?! Why is are the ``3``, ``2``, and ``1`` there in the second call? There's only *one* list for ``acc``'s default value. Each time we call ``insert``, we update that list---and *all* future calls will see it.

There are two solutions:

1. Never mutate a keyword argument. Rather than calling ``acc.insert``, we could write ``acc = [x] + acc`` to create a new list.
2. Use ``None`` as the default, and test at the front to initialize with the mutable value.

Here's an example of both:

.. runner::

    def rev_nomutate(l, acc=[]):
        for x in l:
            acc = [x] + acc
            
        return acc

    print(rev_nomutate([1,2,3]))
    print(rev_nomutate(list("abc")))

    def rev_none(l, acc=None):
        if acc is None:
            acc = []
        
        for x in l:
            acc.insert(0, x)

        return acc

    print(rev_none([1,2,3]))
    print(rev_none(list("abc")))