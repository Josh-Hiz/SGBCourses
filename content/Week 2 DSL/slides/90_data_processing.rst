Data processing
================

Consider the following tabular data:

.. image:: /assets/images/cs515/Week2/image.png

We would like to implement data processing to look up names or phone numbers from a phone directory. In order to do that, it would be convenient if the phone directory data is provided in a structure that Python code can utilize. This unit will cover how to represent data as a **list of dictionaries** and to carry out data processing such as data access, update, and search.

Let's focus on how to represent just a single row of the table above in Python first. Each row includes a name, a phone number, and a state name. To describe this data, we can consider the first name, last name, phone number, and the state as *keys* and the corresponding data as *values*. Therefore, each row can be represented using a dictionary, and the first row, for example, is shown as follows.

.. code-block:: 

    {'first_name': 'James', 'last_name': 'Smith', 'phone_number': 5106423175, 'state': 'CA'}

The information of everyone can be represented similarly using dictionaries.

.. code-block:: 

    {'first_name': 'James', 'last_name': 'Smith', 'phone_number': 5106423175, 'state': 'CA'}
    {'first_name': 'Jennifer', 'last_name': 'Wilson', 'phone_number': 5307521011, 'state': 'OR'}
    {'first_name': 'Robert', 'last_name': 'Jones', 'phone_number': 9498245011, 'state': 'NY'}
    {'first_name': 'Mary', 'last_name': 'Willaims', 'phone_number': 3108254321, 'state': 'TX'}
    {'first_name': 'John', 'last_name': 'Brown', 'phone_number': 2092284400, 'state': 'CA'}
    {'first_name': 'Patricia', 'last_name': 'Miller', 'phone_number': 9518271012, 'state': 'FL'}
    {'first_name': 'Jennifer', 'last_name': 'Davis', 'phone_number': 8585342230, 'state': 'CA'}
    {'first_name': 'Linda', 'last_name': 'Johnson', 'phone_number': 4153537800, 'state': 'GA'}

In order to have the information of everyone in the directory as a single data structure altogether, the dictionaries can be all included in a list by putting them in brackets and separating by commas as follows.

.. code-block:: 

    directory = [{'first_name': 'James', 'last_name': 'Smith', 'phone_number': 5106423175, 'state': 'CA'},
    {'first_name': 'Jennifer', 'last_name': 'Wilson', 'phone_number': 5307521011, 'state': 'OR'},
    {'first_name': 'Robert', 'last_name': 'Jones', 'phone_number': 9498245011, 'state': 'NY'},
    {'first_name': 'Mary', 'last_name': 'Willaims', 'phone_number': 3108254321, 'state': 'TX'},
    {'first_name': 'John', 'last_name': 'Brown', 'phone_number': 2092284400, 'state': 'CA'},
    {'first_name': 'Patricia', 'last_name': 'Miller', 'phone_number': 9518271012, 'state': 'FL'},
    {'first_name': 'Jennifer', 'last_name': 'Davis', 'phone_number': 8585342230, 'state': 'CA'},
    {'first_name': 'Linda', 'last_name': 'Johnson', 'phone_number': 4153537800, 'state': 'GA'}]

Then, we can check that ``directory`` is indeed a list of dictionaries by using the ``type`` function.

Also, we can use the ``len`` function to confirm that the number of people saved in the directory is 8.

.. code-block:: 

    >>> len(directory)
    8

What happens if we apply the ``len`` function to not only the entire list but to each dictionary? It will return the number of key-value pairs, which is 4 in this case because each dictionary has 4 items -- first name, last name, phone number, and state.

.. code-block:: 

    >>> len(directory[0])
    4