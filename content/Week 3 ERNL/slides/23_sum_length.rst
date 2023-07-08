Sum and length
==============

Write a recursive function ``sum_and_length`` that simultaneously computes the sum and the length of an array, returning a list with two elements: the first element is the sum, and the second element is the length.

Let the sum of an empty array be 0. Do *not* use the ``sum`` or ``len`` functions or loops.

Example behavior
----------------

.. code-block::

    >>> sum_and_length([])
    [0, 0]
    >>> sum_and_length([1,2,3])
    [6, 3]
    >>> sum_and_length([1,2,3,4,5,6,7,8,9,10])
    [55, 10]

.. challenge::
    :tester: /_static/cs515_challenges/Week3/Challenge2/test_task.py

    # define sum_and_length
