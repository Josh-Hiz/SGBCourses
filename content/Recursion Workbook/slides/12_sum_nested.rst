Summing nested dictionaries
===========================

Write a function ``sum_nested`` that takes a dictionary ``d`` and sums up every ``int`` and ``float`` inside it, including those in nested dictionaries. You should ignore nested lists or other types. Your code should not use exceptions in any way, i.e., it shouldn't raise any exceptions and shouldn't use ``try``/ ``except``.

Here are some examples:

.. code-block:: 

    >>> d1
    {'a': 1, 'b': '2', 'c': 3}
    >>> sum_nested(d1)
    4
    >>> d2
    {'a': 1, 'b': '2', 'c': {'x': 1, 'y': [4, 5], 'z': 2}}
    >>> sum_nested(d2)
    4
    >>> sum_nested({})
    0

.. challenge::
    :tester: /_static/cs515_challenges/Workbook/Challenge1/test_task.py
    
    # define sum_nested
