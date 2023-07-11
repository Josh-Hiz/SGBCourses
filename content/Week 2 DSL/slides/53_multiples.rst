is_positive_or_multiple_of_7
============================

Write a function called ``is_positive_or_multiple_of_7`` that takes a positive integer ``n`` as its parameter. Write a ``while`` loop in this function that ends if the number ``n`` is a multiple of 7. Otherwise we repeatedly subtract ``n`` by 3, as long as the number ``n`` is positive. Your function returns the final value of n.

For example, if the parameter is given as ``n=100``, then

* your while loop will start because ``n`` is positive.
* As 100 is not a multiple of 7, ``n`` becomes 100-3=97 and the next iteration runs.
* Again, since 97 is not a multiple of 7, it will be reduced to 94.
* In the next iteration, 94 is not a multiple of 7 yet, so ``n`` becomes 94-3=91, and your program goes to the next iteration.
* Finally, 91=7*13 is a multiple of 7, which makes the break statement to end the loop, and your function returns 91.

Sample Input 1:

.. code-block:: 

    100

**Sample Output 1:**

.. code-block:: 
    
    91

**Sample Input 2:**

.. code-block:: 

    14

**Sample Output 2:**

.. code-block::

    14

**Sample Input 3:**

.. code-block:: 

    5

**Sample Output 3:**

.. code-block:: 

    -1

.. challenge::
    :tester: /_static/cs515_challenges/Week2/Challenge19/test_task.py

    # write is_positive_or_multiple_of_7