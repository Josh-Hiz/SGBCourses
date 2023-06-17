Creating dictionaries
=====================

Every element in a dictionary is a **key-value pair** and a dictionary contains a collection of these key-value pairs. A **key-value pair** is some key with its associated value. To create a dictionary, we use curly braces ``{}`` and provide some key-value pair(s) separated by commas. Each key-value pair is created in a dictionary using this syntax ``key:value``. 

Below we have created a dictionary and assigned it to the variable ``class_dict``. This dictionary contains the number of people in this class by their role.

.. code-block:: 

    class_dict = {'instructors': 1, 'CAs': 2, 'students': 59}

Each key is a string that denotes the role. We have 3 keys in ``class_dict`` which represent 3 different roles: ``'instructors'``, ``'CAs'``, and ``'students'``. Each value is an integer that represents the number of people with that particular role. The corresponding values in this dictionary are ``1``, ``2``, and ``59``. After associating the values to the keys, we have 3 key-value pairs: ``'instructors': 1``, ``'CAs': 2``, and ``'students': 59``. Notice that these key-value pairs are within the curly braces and separated by commas. In this ``class_dict`` dictionary, we have 1 instructor, 2 CAs, and 59 students.

Below we have created another dictionary using integers for the key and strings for the value. This ``employees`` dictionary contains employee IDs and the corresponding employee name. Each key is an employee ID and each value is a name. Notice that compared to lists which have indexes that start at 0, dictionary keys can be any integer.

.. code-block:: 

    employees = {2201: 'Joseph Warmus', 548 : 'Annie Wai'}

In this ``employees`` dictionary, we have 2 employees. The employee ID, ``2201``, corresponds to ``'Joseph Warmus'``, and ``548`` corresponds to ``'Annie Wai'``.

The ``dict`` type
-----------------

Dictionaries in Python are of type ``dict``. You can use the type ``dict`` in a few ways: to create or copy a dictionary and in tests with ``isinstance``.

.. runner:: 

    employees = {2201: 'Joseph Warmus', 548 : 'Annie Wai'}

    print(isinstance(employees, dict))

    employees2 = dict(employees)
    print(f'Notice that dict creates a new id: {id(employees)} vs. {id(employees2)}')

    employees3 = dict([(2201, 'Joseph Warmus'), (548, 'Annie Wai')])
    print(employees3)

A dictionary is *like* a list of tuples, but it's much faster to work with keys in dictionaries than it is in lists. Let's learn more!