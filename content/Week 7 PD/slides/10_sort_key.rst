Sort by key
===========

Python's ``list.sort`` method takes a ``key`` keyword parameter. ``key`` defaults to ``None``, in which case the sort uses the conventional order (i.e., ``<=`` or whatever). If ``key`` isn't ``None``, it should be a function that takes elements of the list, which are sorted by their result on ``key``.

Copy and paste in ``mergesort``, and make it take a ``key`` parameter. Here's an example interaction:

.. code-block::

    >>> mergesort(l, key=get_id)
    [{'id': 73, 'name': 'Wen-Ding'}, {'id': 100, 'name': 'Michael'}, {'id': 112, 'name': 
    'Anvay'}]
    >>> mergesort(l, key=get_name)
    [{'id': 112, 'name': 'Anvay'}, {'id': 100, 'name': 'Michael'}, {'id': 73, 'name': 'We
    n-Ding'}]

.. challenge::
    :tester:

    # copy in mergesort here

    l = [{'id': 100, 'name': 'Michael'},
         {'id': 73, 'name': 'Wen-Ding'},
         {'id': 112, 'name': 'Anvay'}]

    def get_id(r): return r['id']
    def get_name(r): return r['name']

    print(mergesort(l, key=get_id))
    print(mergesort(l, key=get_name))