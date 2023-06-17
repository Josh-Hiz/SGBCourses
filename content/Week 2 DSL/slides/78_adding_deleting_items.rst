Methods for adding and deleting items
=====================================

dict.update()
-------------

This method adds key-value pairs to the dictionary. The method takes in either another dictionary or an iterable (like a list) of key-value pairs and it adds those key-value pairs into the dictionary. 

Consider our previous example ``class_dict``:

.. code-block::

    >>> class_dict
    {'instructors': 2, 'TAs': 10, 'tutors': 35, 'students': 600}

Let's add two more key-value pairs which gives the number of head tutors and the number of sections for this class to this dictionary. We can use the ``update()`` method to add the key-value pair as follows. As you can see below, we have used another **dictionary** containing the two key-value pairs as the input parameter for the ``update()`` method.

.. code-block:: 

    >>> new_entries_dict = {'head_tutors': 3, 'sections': 4}
    >>> class_dict.update(new_entries_dict)

    >>> class_dict
    {'instructors': 2, 'TAs': 10, 'tutors': 35, 'students': 600, 'head_tutors': 3, 'sections': 4}

Alternatively, you can also use a **list** of two-value tuples as the input parameter to the ``update()`` method.

.. code-block:: 

    >>> new_entries_list = [('head_tutors', 3), ('sections', 4)]
    >>> class_dict.update(new_entries_list)

    >>> class_dict
    {'instructors': 2, 'TAs': 10, 'tutors': 35, 'students': 600, 'head_tutors': 3, 'sections': 4}

dict.pop()
----------

This method removes the key-value pair from the dictionary and returns its value. The input parameter to the method should be the **key** present in the dictionary.

Let's delete the two newly added key-value pairs which give the number of head tutors and the number of sections for this class from the above dictionary. We need to provide the keys '**head_tutors**' and '**sections**' one after the other to delete them from the dictionary.

.. code-block:: 

    >>> class_dict
    {'instructors': 2, 'TAs': 10, 'tutors': 35, 'students': 600, 'head_tutors': 3, 'sections': 4}

    >>> class_dict.pop('head_tutors')
    3

    >>> class_dict
    {'instructors': 2, 'TAs': 10, 'tutors': 35, 'students': 600, 'sections': 4}

    >>> class_dict.pop('sections')
    4

    >>> class_dict
    {'instructors': 2, 'TAs': 10, 'tutors': 35, 'students': 600}

As you can see above, the ``pop()`` method returns the value that was associated with the key given as the input parameter. When we print the class_dict dictionary again, we see that the key-value pair associated with key given as input parameter is deleted.