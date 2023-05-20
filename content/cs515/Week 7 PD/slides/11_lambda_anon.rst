Anonymous functions with lambda
===============================

So far, we've used ``def`` to define functions. It can get a little silly when the functions are short, like our ``get_id`` and ``get_name`` examples. Python supports **anonymous functions** using the lambda keyword (borrowed from the `lambda calculus <https://en.wikipedia.org/wiki/Lambda_calculus>`_). Here's an example:

.. exec_code::

    f = lambda x: x + 1

    print(f(5))
    print(f(10))

Notice that we don't need to write a ``return`` here: when using ``lambda``, you just write an expression, and that's what is returned. If you find yourself writing a ``lambda`` that does a lot... then it's time to break out ``def`` and write a fuller function. Lambda functions are best for short bits of code, like when calling ``map`` or ``filter`` or ``list.sort``:

.. exec_code::

    l = [{'id': 100, 'name': 'Michael'},
     {'id': 73, 'name': 'Wen-Ding'},
     {'id': 112, 'name': 'Anvay'}]

    print(f'The original list is:\n\t{l}')
    l.sort(key=lambda r: r['id'])
    print(f'Sorted by id the list is:\n\t{l}')
    l.sort(key=lambda r: r['name'])
    print(f'Sorted by name the list is:\n\t{l}')