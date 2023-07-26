Nested modules
==============

You can define modules inside of other modules. A directory ``algorithms`` holding files ``sort.py`` and ``search.py`` will generate a module ``algorithms`` with **sub-modules** ``algorithms.sort`` and ``algorithms.search``.

To make sure that Python treats such directories correctly, you should create a file ``__init__.py`` in the directory. The ``__init__.py`` file can be empty; ours prints out "Loading algorithms!". Notice how many times it prints---when you add an import, does it print again, or no?

In the example below, we've started out building the directory ``algorithms`` and the ``search.py`` module, along with a ``main.py`` that imports from both the ``algorithms.search`` and ``algorithms.sort`` modules. Create the ``sort.py`` file with the definition ``mergesort``; change ``main.py`` to import that definition.

Paste the following code into ``algorithms/__init__.py``:

.. code-block::

    print("Loading algorithms!")

Paste the following code into ``algorithms/search.py``:

.. code-block::

    def linear_search(v, l):
        i = 0
        for x in l:
            if x == v:
                return i
            i = i + 1
        raise ValueError(f'{v} not found')
        
    def binary_search(v, l):
        lo = 0
        hi = len(l) - 1
        while lo <= hi:
            mid = lo + ((hi - lo) // 2) # what goes wrong if we use / ?
    #        print(f'looking at {mid} between {lo} and {hi}')
            x = l[mid]
            if   v == x: return mid
            elif v <  x: hi = mid - 1
            elif v >  x: lo = mid + 1
        raise ValueError(f'{v} not found')

Complete ``sort.py`` and ``main.py``

.. challenge::
    :files:
        algorithms/__init__.py
        algorithms/search.py
        algorithms/sort.py
        main.py