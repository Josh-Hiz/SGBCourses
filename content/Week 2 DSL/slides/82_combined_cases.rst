combined_cases
==============

Write a function ``combined_cases(day1_cases, day2_cases)`` which take in two input parameters which are two dictionaries that represent the COVID-19 cases on one specific day in different states in the USA. Your function should return a dictionary that contains the sum of the cases of the two days in the given states. 

For example:

If the following two dictionaries are given as input:

.. code-block:: 

    day1_cases = {'Texas': 10678, 'Florida': 7459, 'Illinois': 12601}
    day2_cases = {'Texas': 13379, 'Florida': 7925, 'Illinois': 11301}

Then your function must return:

.. code-block:: 

    {'Texas': 24057, 'Florida': 15384, 'Illinois': 23902}

**Sample Input:**

.. code-block:: 

    {'California': 10577, 'New York': 5167}
    {'California': 11835, 'New York': 5364}

**Sample Output:**

.. code-block:: 

    {'California': 22412, 'New York': 10531}

.. challenge::

    # define combined_cases(day1_cases, day2_cases)

    # here are some tests (feel free to add your own)

    assert combined_cases({'Texas': 10678, 'Florida': 7459, 'Illinois': 12601}, {'Texas': 13379, 'Florida': 7925, 'Illinois': 11301}) == {'Texas': 24057, 'Florida': 15384, 'Illinois': 23902}

    assert combined_cases({'California': 10577, 'New York': 5167}, {'California': 11835, 'New York': 5364}) == {'California': 22412, 'New York': 10531}