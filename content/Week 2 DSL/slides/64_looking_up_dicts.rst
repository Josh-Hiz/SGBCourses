Looking things up in a dictionary
=================================

Recall that we can index a list with square brackets ``[]`` to obtain an element at a particular index.

.. code-block:: 

    numbers = [2, 5, 1, 6, 10]
    numbers[3]

Similarly, we can do the same with dictionaries. Instead of providing an index, we can provide a key. Below we have created a ``class_dict`` dictionary that contains the number of people in this class by their role. If we want to get the number of CAs, we can access it using square brackets with the key for tutors, ``class_dict['CAs']``. (remember to include quotes since ``'CAs'`` is a string)

.. runner:: 

    class_dict = {'instructors': 1, 'CAs': 2, 'students': 59}
    num_cas = class_dict['CAs']
    print(num_cas)

The above code prints out 2 which is the corresponding value for the key ``'CAs'``.

.. code-block::

    35

Below is another example with a dictionary that contains employee IDs with employee names. In this example, we wanted the name of the employee that corresponds to the employee ID, 2201. To obtain the employee name corresponding to this employee ID, we provided the key (i.e., employee ID) in square brackets.

.. runner:: 

    employees = {2201 : 'Joseph Warmus', 548: 'Annie Wai'}
    name = employees[2201]
    print(name)

The above code prints out Joseph Warmus which is the value associated with the key, 2201.

.. code-block::

    Joseph Warmus

Just like for a list, looking up keys that don't exist produce an error. While bad indices to lists and strings raise an ``IndexError``, bad indexes for dictionaries produce a ``KeyError``.

.. runner:: 

    class_dict = {'instructors': 1, 'CAs': 2, 'students': 59}
    class_dict['auditors']

Here's the output:

.. code-block:: 

    Traceback (most recent call last):
    File "/home/main.py", line 2, in <module>
        class_dict['auditors']
    KeyError: 'auditors'