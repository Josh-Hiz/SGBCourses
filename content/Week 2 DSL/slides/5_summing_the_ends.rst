Summing the Ends
================

Write a function ``sum_of_ends`` that takes a list of numbers as an input parameter and:

* if the list is empty, returns ``0``
* if the list is not empty, returns the sum of the first element (at index 0) and the last element (at index length - 1)
* Note that for a list with only one element, the first element and the last element would be the same one element in the list and thus the function should return the sum of the element with itself. ex: If ``a= [10]`` then the ``sum_of_ends`` function should return ``20``.

We have written the code in the backend already that reads in the input for you and turns it into a list of numbers, and prints results after. Your only task is to write the function ``sum_of_ends``. 

You can pick everything about the parameter name and how you write the body of the function, but it must be called ``sum_of_ends``.

The code challenge will call your ``sum_of_ends`` function with different lists and check that it behaves correctly on all of them.

**Sample Input 1:**

``8 11 12``

**Sample Output 1:**

``20``

**Sample Input 2:**

``5``

**Sample Output 2:**

``10``

**Sample Input 3:**

``7 8 9 10 11``

**Sample Output 3:**

``18``

.. challenge::
    :tester: /_static/cs515_challenges/Week2/Challenge1/test_task.py

    # define sum_of_ends here