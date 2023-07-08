Type errors
===========

In Python, it's possible to get a type error at runtime by combining values in the wrong way. Here's an example:

.. runner:: 

    print('hello')

    def add3(n):
        return n + 3

    print('the first result is', add3(5))
    print('the second result is', add3('uh oh'))
    print('goodbye')

Like a ``NameError``, the ``TypeError`` we get here is *latent*, hiding until a bad value comes in. When we pass ``5`` to ``add3``, there's no problem; but when we pass ``'uh oh'`` to ``add3`` the ``+`` operation doesn't know how to combine an int and a str, so we get a ``TypeError``. Like the ``NameError``, the program stops just as soon as the error occurs.