find_mode
=========

Using the previous code as a guide, define a function ``find_mode`` that takes a list of numbers as input and returns the mode as output.

Notice that our previous solution will return 0 if the dictionary is empty. However this is incorrect, because 0 is not the mode if our list of numbers is empty. Update the following function ``find_mode`` such that it returns ``None`` if the dictionary is empty.

If there's a tie, the input is "multimodal" and properly we should return a list. Your code can return any of the modal items.

**Sample Input 1:**

.. code-block:: 

    [5, 5, 6, 4, 7, 8, 5, 6]

**Sample Output 1:**

.. code-block:: 

    5

**Sample Input 2:**

.. code-block::
    
    []

**Sample Output 2:**

.. code-block::
    
    None

.. challenge::

    # define find_mode(nums)

    # here are some tests

    assert find_mode([5, 5, 6, 4, 7, 8, 5, 6]) == 5
    assert find_mode([1,1,1,2,2,2,2]) == 2
    assert find_mode([]) == None
