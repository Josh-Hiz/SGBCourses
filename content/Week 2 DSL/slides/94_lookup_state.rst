lookup_state
============

Recall that we have a phone directory as seen here.

.. code-block:: 

    directory = [{'first_name': 'James', 'last_name': 'Smith', 'phone_number': 5106423175, 'state': 'CA'},
    {'first_name': 'Jennifer', 'last_name': 'Wilson', 'phone_number': 5307521011, 'state': 'OR'},
    {'first_name': 'Robert', 'last_name': 'Jones', 'phone_number': 9498245011, 'state': 'NY'},
    {'first_name': 'Mary', 'last_name': 'Willaims', 'phone_number': 3108254321, 'state': 'TX'},
    {'first_name': 'John', 'last_name': 'Brown', 'phone_number': 2092284400, 'state': 'CA'},
    {'first_name': 'Patricia', 'last_name': 'Miller', 'phone_number': 9518271012, 'state': 'FL'},
    {'first_name': 'Jennifer', 'last_name': 'Davis', 'phone_number': 8585342230, 'state': 'CA'},
    {'first_name': 'Linda', 'last_name': 'Johnson', 'phone_number': 4153537800, 'state': 'GA'}]

Define a function ``lookup_state`` that takes ``state`` as its parameter, which is a string that denotes the abbreviation of a state name, and returns a list of full names that is associated with ``state``. Please note that ``directory`` is a global variable, and you should not use ``input()`` or ``print()`` to control the input or output. You only have to define a function.

**Sample Input:**

.. code-block::

    CA

**Sample Output:**

.. code-block:: 

    ['James Smith', 'John Brown', 'Jennifer Davis']

.. challenge::

    directory = [{'first_name': 'James', 'last_name': 'Smith', 'phone_number': 5106423175, 'state': 'CA'},
    {'first_name': 'Jennifer', 'last_name': 'Wilson', 'phone_number': 5307521011, 'state': 'OR'},
    {'first_name': 'Robert', 'last_name': 'Jones', 'phone_number': 9498245011, 'state': 'NY'},
    {'first_name': 'Mary', 'last_name': 'Willaims', 'phone_number': 3108254321, 'state': 'TX'},
    {'first_name': 'John', 'last_name': 'Brown', 'phone_number': 2092284400, 'state': 'CA'},
    {'first_name': 'Patricia', 'last_name': 'Miller', 'phone_number': 9518271012, 'state': 'FL'},
    {'first_name': 'Jennifer', 'last_name': 'Davis', 'phone_number': 8585342230, 'state': 'CA'},
    {'first_name': 'Linda', 'last_name': 'Johnson', 'phone_number': 4153537800, 'state': 'GA'}]

    # define lookup_state(state)

    # a test to make things easy for you
    assert lookup_state('CA') == ['James Smith', 'John Brown', 'Jennifer Davis']