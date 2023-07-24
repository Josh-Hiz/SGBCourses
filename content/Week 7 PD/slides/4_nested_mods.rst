Nested modules
==============

You can define modules inside of other modules. A directory ``algorithms`` holding files ``sort.py`` and ``search.py`` will generate a module ``algorithms`` with **sub-modules** ``algorithms.sort`` and ``algorithms.search``.

To make sure that Python treats such directories correctly, you should create a file ``__init__.py`` in the directory. The ``__init__.py`` file can be empty; ours prints out "Loading algorithms!". Notice how many times it prints---when you add an import, does it print again, or no?

In the example below, we've started out building the directory ``algorithms`` and the ``search.py`` module, along with a ``main.py`` that imports from both the ``algorithms.search`` and ``algorithms.sort`` modules. Create the ``sort.py`` file with the definition ``mergesort``; change ``main.py`` to import that definition.

.. challenge::
    :files:
        algorithms/__init__.py
        algorithms/search.py
        algorithms/sort.py
        main.py