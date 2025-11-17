Creating objects: constructors
==============================

To create an object, you must use a constructor. Python offers shortcuts for many of its objects: for ``str``, we just use ``'string notation'``, and ``list`` and ``dict`` have their own notations, too. But user-defined classes can be **instantiated** into objects using a **constructor**. Here 'constructor' is a fancy word for "a function that returns a new object".

We've already seen constructors used: when we raise an exception, we write ``raise ValueError('something went wrong')``. The argument to the ``raise`` keyword is a call to the ``ValueError`` constructor.

In Python, a type/class and its constructor are one and the same thing. The functions ``str`` and ``list`` and ``dict`` we've seen are the type names for those types, but they're also the constructors, i.e., calling them will create new strings and lists and dictionaries.

.. code-block:: 

    >>> str
    <class 'str'>
    >>> list
    <class 'list'>
    >>> dict
    <class 'dict'>
    >>> str('hi')
    'hi'
    >>> str(5)
    '5'
    >>> list("hello there")
    ['h', 'e', 'l', 'l', 'o', ' ', 't', 'h', 'e', 'r', 'e']
    >>> list()
    []

Notice that the constructors here are *very* versatile. Since these types are special, it's perhaps clearer to see an example with the various classes of exception and error we've seen:

.. code-block:: 

    >>> v = ValueError('hi there')
    >>> v
    ValueError('hi there')
    >>> v2 = ValueError('another one')
    >>> v2
    ValueError('another one')
    >>> v3 = ValueError()
    >>> v3
    ValueError()
