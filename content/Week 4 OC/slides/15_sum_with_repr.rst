Sum with ``__repr__``
=====================

Define a class ``Sum`` with a constructor that takes two arguments, ``left``, and ``right``. The constructor should set corresponding fields on the object, i.e., the field ``left`` should get the value from ``left`` and the field ``right`` should get the value from ``right``. You should set a third field, ``sum``, that is equal to the sum of the two fields.

Define a ``__repr__`` method that reproduces the constructor, i.e.,

.. code-block:: 
    
    >>> Sum(1, 2)
    Sum(1, 2)

and a ``__str__`` method that shows the sum, i.e.,

.. code-block:: 

    >>> print(Sum(1, 2))
    1 + 2 = 3

.. challenge:: 
    :tester: /_static/cs515_challenges/Week4/Challenge4/test_task.py

    # define the Sum class