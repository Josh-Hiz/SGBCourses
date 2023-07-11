print_numbers
=============

Write a function called ``print_numbers`` that has a list of integers called ``my_list`` as its parameter. Using a ``continue`` statement and a ``for`` loop, the function prints every number in ``my_list`` except for multiples of 3.

(This function could be written lots of ways, but we'd like to you practice using ``continue``. It's a good exercise to try others, though. Can you do it without ``continue`` but with a ``for`` loop? Can you do it with a ``filter`` and an unconditional for loop?)

**Sample Input 1:**

.. code-block:: 

    2 5 36 53 31

**Sample Output 1:**

.. code-block:: 

    2
    5
    53
    31

**Sample Input 2:**

.. code-block::

    3 6 9 12 5 2 1

**Sample Output 2:**

.. code-block:: 

    5
    2
    1

.. challenge:: 
    :tester: /_static/cs515_challenges/Week2/Challenge21/test_task.py

    # define print_numbers
