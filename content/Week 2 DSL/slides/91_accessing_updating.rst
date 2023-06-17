Accessing and updating data
===========================

In the previous step, we learned how to represent the directory data as a list of dictionaries.

.. code-block:: 

    directory = [{'first_name': 'James', 'last_name': 'Smith', 'phone_number': 5106423175, 'state': 'CA'},
    {'first_name': 'Jennifer', 'last_name': 'Wilson', 'phone_number': 5307521011, 'state': 'OR'},
    {'first_name': 'Robert', 'last_name': 'Jones', 'phone_number': 9498245011, 'state': 'NY'},
    {'first_name': 'Mary', 'last_name': 'Willaims', 'phone_number': 3108254321, 'state': 'TX'},
    {'first_name': 'John', 'last_name': 'Brown', 'phone_number': 2092284400, 'state': 'CA'},
    {'first_name': 'Patricia', 'last_name': 'Miller', 'phone_number': 9518271012, 'state': 'FL'},
    {'first_name': 'Jennifer', 'last_name': 'Davis', 'phone_number': 8585342230, 'state': 'CA'},
    {'first_name': 'Linda', 'last_name': 'Johnson', 'phone_number': 4153537800, 'state': 'GA'}]

Now, let's implement code to access the partial information we want from the directory. Note that the type of ``directory`` is list. Therefore, each element of the list can be extracted by indexing with brackets, just as we handle any other simple lists. For example, if the directory at index 0 is inquired, then the following code can be used.

.. code-block:: 

    >>> directory[0]
    {'first_name': 'James', 'last_name': 'Smith', 'phone_number': 5106423175, 'state': 'CA'}

If the last element of the directory is requested, then we can use the following ways.

.. code-block:: 

    >>> directory[7]
    {'first_name': 'Linda', 'last_name': 'Johnson', 'phone_number': 4153537800, 'state': 'GA'}
    >>> directory[-1]
    {'first_name': 'Linda', 'last_name': 'Johnson', 'phone_number': 4153537800, 'state': 'GA'}
    >>> directory[len(directory)-1]
    {'first_name': 'Linda', 'last_name': 'Johnson', 'phone_number': 4153537800, 'state': 'GA'}

Also, we can extract multiple dictionaries with slicing. When we would like to have a list of the dictionaries at index 2, 3, and 4, then our code can be written as follows.

.. code-block:: 

    >>> directory[2:5]
    [{'first_name': 'Robert', 'last_name': 'Jones', 'phone_number': 9498245011, 'state': 'NY'},
    {'first_name': 'Mary', 'last_name': 'Willaims', 'phone_number': 3108254321, 'state': 'TX'},
    {'first_name': 'John', 'last_name': 'Brown', 'phone_number': 2092284400, 'state': 'CA'}]

``directory[i]`` can extract the dictionary at the index ``i`` as long as ``i`` is a valid index. Using an index out of range will result in IndexError as seen in the following example.

.. code-block:: 

    >>> directory[8]
    Traceback (most recent call last):
    File "<pyshell#18>", line 1, in <module>
        directory[8]
    IndexError: list index out of range

Now that we know how to access a dictionary in the list, let's try accessing a specific key-value pair. Since ``directory[i]`` is a dictionary for any valid index ``i``, we are able to access each item in the dictionary by adding brackets with a key inside as follows.

.. code-block:: 

    >>> directory[0]['first_name']
    'James'
    >>> directory[1]['last_name']
    'Wilson'
    >>> directory[2]['phone_number']
    9498245011
    >>> directory[3]['state']
    'TX'

The index inside the first pair of brackets corresponds to the index of a dictionary as an element in the entire list. The key inside the second pair of brackets is decided up to which key-value pair you are looking for within the chosen dictionary. To be specific, a required value can be obtained by running the code ``directory[i][key]``, where ``i`` is a valid index among ``0``, ``1``,..., ``7`` or ``-1``, ``-2``,..., ``-8`` and ``key`` is chosen among ``'first_name'``, ``'last_name'``, ``'phone_number'``, and ``'state'``. However, using an inadequate key leads to KeyError as seen in the following example.

.. code-block:: 

    >>> directory[0]['zip_code']
    Traceback (most recent call last):
    File "<pyshell#19>", line 1, in <module>
        directory[0]['zip_code']
    KeyError: 'zip_code'

We can avoid KeyError by utilizing the ``get`` method in order to get the value returned according to the specified key. For any valid index ``i``, the command ``directory[i].get(key)`` returns the requested value that corresponds to ``key`` as follows.

.. code-block:: 

    >>> directory[4].get('first_name')
    'John'
    >>> directory[5].get('last_name')
    'Miller'
    >>> directory[6].get('phone_number')
    8585342230
    >>> directory[7].get('state')
    'GA'

If the command is used with a key that does not exist, then it returns None.

.. code-block:: 

    >>> print(directory[0].get('zip_code'))
    None

On top of accessing specific information, we can update it with indexing properly. If it is required to update an item in a particular dictionary, then we use the same indexing method as access and use the assignment operator ``=`` followed by the value to update. For example, assume that we would like to update the phone number of the dictionary at index 1. Then, the following ways update the phone number.

.. code-block:: 

    >>> directory[1]['phone_number'] = 8585343213
    >>> directory[1].update({'phone_number': 8585343213})

Also, we can update the directory by adding information for a new person. Since the data type of the entire directory is a list, we can use the ``append`` method to add a dictionary representing information of the new person. For example, the following code extends the directory.

.. code-block:: 

    >>> directory.append({'first_name': 'Maria', 'last_name': 'Garcia', 'phone_number': 8058938000, 'state': 'NV'})

We can confirm that the ``directory`` is updated as follows.

.. code-block:: 

    >>> directory
    [{'first_name': 'James', 'last_name': 'Smith', 'phone_number': 5106423175, 'state': 'CA'},
    {'first_name': 'Jennifer', 'last_name': 'Wilson', 'phone_number': 8585343213, 'state': 'OR'},
    {'first_name': 'Robert', 'last_name': 'Jones', 'phone_number': 9498245011, 'state': 'NY'},
    {'first_name': 'Mary', 'last_name': 'Willaims', 'phone_number': 3108254321, 'state': 'TX'},
    {'first_name': 'John', 'last_name': 'Brown', 'phone_number': 2092284400, 'state': 'CA'},
    {'first_name': 'Patricia', 'last_name': 'Miller', 'phone_number': 9518271012, 'state': 'FL'},
    {'first_name': 'Jennifer', 'last_name': 'Davis', 'phone_number': 8585342230, 'state': 'CA'},
    {'first_name': 'Linda', 'last_name': 'Johnson', 'phone_number': 4153537800, 'state': 'GA'},
    {'first_name': 'Maria', 'last_name': 'Garcia', 'phone_number': 8058938000, 'state': 'NV'}]

