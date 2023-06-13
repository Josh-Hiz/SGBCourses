Hip to be square
================

Write a function called ``square(lst)`` that takes one parameter which is a list of integers and returns a list that contains the square of each element in the given list (see the sample inputs for some examples). 

We have written the code to read the input from the user in the background. Also, the code challenge will call your function with many input lists and check that it behaves correctly on all of them. Your task is to only define the function as specified which will return the new list which contains the squares of each element.

(Just as the last challenge did what ``in`` does, this challenge does what ``map`` does. But I'd like you to use ``for`` loop, for practice!)

**Sample Input 1:**

.. code-block::

    1 2 3 4

**Sample Output 1:**

.. code-block:: 

    [1, 4, 9, 16]

**Sample Input 2:**

.. code-block::

    10 12 15

**Sample Output 2:**

.. code-block:: 

    [100, 144, 225]

.. challenge:: 
    :tester: /_static/cs515_challenges/Week2/Challenge14/test_task.py

    # define square
    #
    # use a for loop, not map!