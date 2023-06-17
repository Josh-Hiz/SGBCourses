insert_pair
===========

Implement a function ``insert_pair`` that takes in a ``dictionary``, ``key``, and ``value`` and adds the new ``key`` and ``value`` pair to ``dictionary``. Your function should **return** the resulting dictionary.

For example, if ``dictionary = {'instructors': 2, 'TAs': 10, 'tutors': 35, 'students': 600}``, ``key = 'head tutors'``, and ``value = 2``. Your function should return the following dictionary.

``{'instructors': 2, 'TAs': 10, 'tutors': 35, 'students': 600, 'head tutors': 2}``

**Sample Input 1:**

{'instructors': 2, 'TAs': 10, 'tutors': 35, 'students': 600}
head tutors
2

**Sample Output 1:**

.. code-block:: 

    {'instructors': 2, 'TAs': 10, 'tutors': 35, 'students': 600, 'head tutors': 2}

**Sample Input 2:**

.. code-block:: 

    {'CSE': 4, 'MATH': 10}
    BIO
    4

**Sample Output 2:**

.. code-block:: 

    {'CSE': 4, 'MATH': 10, 'BIO': 4}

**Sample Input 3:**

.. code-block:: 
        
    {}
    10
    2

**Sample Output 3:**

.. code-block:: 

    {10: 2}

.. challenge::

    # define insert_pair(dictionary, key, value)

    # we've copied the samples here as tests
    # feel free to add your own

    # to be clear, if nothing is printed after completing the challenge, 
    # that means you did it correctly in this case!
    assert insert_pair({'instructors': 2, 'TAs': 10, 'tutors': 35, 'students': 600}, 'head tutors', 2) == {'instructors': 2, 'TAs': 10, 'tutors': 35, 'students': 600, 'head tutors': 2}, "sample 1"

    assert insert_pair({'CSE': 4, 'MATH': 10}, 'BIO', 4) == {'CSE': 4, 'MATH': 10, 'BIO': 4}

    assert insert_pair({}, 10, 2) == {10: 2}