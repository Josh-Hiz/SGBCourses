Actually processing the data
============================

.. code-block:: 
    
    directory = [{'first_name': 'James', 'last_name': 'Smith', 'phone_number': 5106423175, 'state': 'CA'},
    {'first_name': 'Jennifer', 'last_name': 'Wilson', 'phone_number': 5307521011, 'state': 'OR'},
    {'first_name': 'Robert', 'last_name': 'Jones', 'phone_number': 9498245011, 'state': 'NY'},
    {'first_name': 'Mary', 'last_name': 'Willaims', 'phone_number': 3108254321, 'state': 'TX'},
    {'first_name': 'John', 'last_name': 'Brown', 'phone_number': 2092284400, 'state': 'CA'},
    {'first_name': 'Patricia', 'last_name': 'Miller', 'phone_number': 9518271012, 'state': 'FL'},
    {'first_name': 'Jennifer', 'last_name': 'Davis', 'phone_number': 8585342230, 'state': 'CA'},
    {'first_name': 'Linda', 'last_name': 'Johnson', 'phone_number': 4153537800, 'state': 'GA'}]

Define a function that looks up a phone number 
----------------------------------------------

We will define a function that is given a phone number as an integer parameter and returns the corresponding full name. Since the code has to iterate over each dictionary until it finds the person with the referred phone number, a ``for`` loop is used as follows. Note that a name can be returned once the referred number is found, because no two people have the same phone number.

.. code-block:: python

    def find_name(reference):
        for person in directory:
            # if the phone number of this person matches reference, 
            # return the full name

In the body part of the ``for`` loop, we have to access the phone number of the current iteration and check if it matches the referred number. So, the framework above can be filled as follows.

.. code-block:: python

    def find_name(reference):
        for person in directory:
            if person['phone_number'] == reference:
                # return the full name

Only the dictionary with the matching phone number will fall into the body part of the ``if`` statement, in which case we can return the according full name. We can use string concatenation to generate the full name.

.. code-block:: python

    def find_name(reference):
        for person in directory:
            if person['phone_number'] == reference:
                return person['first_name'] + ' ' + person['last_name']

Now, the function is completely written and we can utilize our function.

.. code-block:: 

    >>> find_name(8585343213)
    'Jennifer Wilson'
    >>> find_name(8585342230)
    'Jennifer Davis'

Define a function that looks up a first name
--------------------------------------------

We will define a function that is given a first name as a string parameter and returns a list of every phone number that corresponds to the name. Since the code has to iterate over each dictionary to check whether each person has the referred name, a ``for`` loop is used as follows. The number of dictionaries with the matching name may vary up to what name is referred.

.. code-block:: python

    def find_number(reference):
        result = []
        for person in directory:
            # if the first name of this person matches reference, 
            # add the phone number
        return result
    
In the body part of the ``for`` loop, we have to access the first name of the current iteration and check if it matches the referred name. So, the framework above can be filled in as follows.

.. runner::

    directory = [
        {'first_name': 'James', 'last_name': 'Smith', 'phone_number': 5106423175, 'state': 'CA'},
        {'first_name': 'Jennifer', 'last_name': 'Wilson', 'phone_number': 5307521011, 'state': 'OR'},
        {'first_name': 'Robert', 'last_name': 'Jones', 'phone_number': 9498245011, 'state': 'NY'},
        {'first_name': 'Mary', 'last_name': 'Willaims', 'phone_number': 3108254321, 'state': 'TX'},
        {'first_name': 'John', 'last_name': 'Brown', 'phone_number': 2092284400, 'state': 'CA'},
        {'first_name': 'Patricia', 'last_name': 'Miller', 'phone_number': 9518271012, 'state': 'FL'},
        {'first_name': 'Jennifer', 'last_name': 'Davis', 'phone_number': 8585342230, 'state': 'CA'},
        {'first_name': 'Linda', 'last_name': 'Johnson', 'phone_number': 4153537800, 'state': 'GA'}
        ]

    def find_numbers(reference):
        result = []
        for person in directory:
            if person['first_name'] == reference:
                result.append(person['phone_number'])
        return result

    print(find_numbers('Jennifer'))
    print(find_numbers('John'))
    print(find_numbers('Michael'))

Our function is now completely written, and we can use this function as follows. We can see that there are two phone numbers for 'Jennifer' because there are people with the first name Jennifer: Jennifer Wilson and Jennifer Davis. 

.. code-block:: 

    >>> find_numbers('Jennifer')
    [8585343213, 8585342230]
    >>> find_numbers('John')
    [2092284400]
    >>> find_numbers('Michael')
    []