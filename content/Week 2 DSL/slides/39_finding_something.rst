Finding something in a list
===========================

The following function ``contains_2(lst)`` is partially complete. Replace each **CHANGEME** such that the function returns ``True`` once it finds a 2 in ``lst``, or ``False`` if there is no 2 in ``lst``. You can assume ``lst`` is a list of integer values.

Hint: for the first **CHANGEME** you will decide the name of this variable.

(You might think... can't I just use ``in`` to do that? Indeed you can... but I'd like you to implement your *own* version of ``in``!)

Sample Input 1:

.. code-block:: 

    5 3 2 8

**Sample Output 1:**

.. code-block:: 

    True

**Sample Input 2:**

.. code-block:: 

    2 6

**Sample Output 2:**

.. code-block:: 

    True

**Sample Input 3:**

.. code-block:: 

    1 3 5 7 9

**Sample Output 3:**

.. code-block:: 

    False

.. challenge:: 
    :tester: /_static/cs515_challenges/Week2/Challenge13/test_task.py

    def contains_2(lst):
        # NB you may have to pick a variable name for this first one!
        for CHANGEME in lst:
            if CHANGEME: 
                return CHANGEME
        return CHANGEME