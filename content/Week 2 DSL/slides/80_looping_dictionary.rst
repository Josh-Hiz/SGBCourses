Looping over dictionaries
=========================

1. Using the ``in`` keyword for a ``for`` loop
----------------------------------------------

We have learned in previous lessons that ``for`` loops with a dictionary can iterate over each key in the dictionary. With our example ``class_dict``, we can repeatedly print the keys with a ``for`` loop.

.. code-block:: 

    class_dict = {'instructors': 2, 'TAs':10, 'tutors':35, 'students': 600}
    for member in class_dict:
        print(member)

Here is the output of the keys printed.

.. code-block:: 

    instructors
    TAs
    tutors
    students

In case that we want to print the values instead of the keys, our code can be edited as

.. code-block:: 

    class_dict = {'instructors': 2, 'TAs':10, 'tutors':35, 'students': 600}
    for member in class_dict:
        print(class_dict[member])

and the output is as follows.

.. code-block:: 

    2
    10
    35
    600

2. Dictionary methods for repetitive access of contents
-------------------------------------------------------

However, we can use dictionary methods to iteratively access keys, values, or their pairs.

dict.keys()
-----------

The ``keys()`` method returns a collection of keys in the dictionary that the method is called upon. Therefore, we can use a ``for`` loop and the ``keys()`` method to access every key as follows:

.. code-block:: 

    class_dict = {'instructors': 2, 'TAs':10, 'tutors':35, 'students': 600}
    for member in class_dict.keys():
        print(member)

The output is given as

.. code-block:: 

    instructors
    TAs
    tutors
    students

dict.values()
-------------

The ``values()`` method can be utilized in the same format to access corresponding values in the given dictionary. It returns a collection of values in the dictionary, and accordingly, using a ``for`` loop with the ``values()`` method enables to handle every value in the dictionary.

.. code-block:: 

    class_dict = {'instructors': 2, 'TAs':10, 'tutors':35, 'students': 600}
    for num in class_dict.values():
        print(num)

Here is the output.

.. code-block:: 

        2
        10
        35
        600

This is useful when we are required to print every value in the dictionary.

dict.items()
------------

What if it is necessary to acknowledge in the output which key is associated to each value? The ``items()`` method comes in handy when we want to access every key-value pair. It returns a collection of every pair in the dictionary, where each pair is a **tuple** of a key and a value.

.. code-block:: 

    class_dict = {'instructors': 2, 'TAs':10, 'tutors':35, 'students': 600}
    for num in class_dict.items():
        print(pair)

The output of this ``for`` loop is

.. code-block:: 

    ('instructors', 2)
    ('TAs', 10)
    ('tutors', 35)
    ('students', 600)