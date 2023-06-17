How big is the dictionary?
==========================

Recall that we use the ``len()`` function to compute the number of characters in a string or to compute the number of elements in a list. For example,

.. code-block:: 

    >>> my_string = 'CS 515-A'
    >>> len(my_string)
    8

    >>> my_list = ['Python', 'Java', 'C++', 'R']
    >>> len(my_list)
    4

The above code for a string and a list have in common that the ``len()`` function returns the number of items included in a given collection. We can use the ``len()`` function in a similar way for dictionaries as well, considering that a dictionary is a collection of key-value pairs. 

Let's take a look at the following dictionary that maps each type of member in our class with their respective numbers.

.. code-block:: 
    
    class_dict = {'instructors': 2, 'TAs': 10, 'tutors': 35, 'students': 600}

We can see that the dictonary ``class_dict`` consists of the following 4 key-value pairs:

* ``'instructors': 2``

* ``'TAs': 10``

* ``'tutors': 35``

* ``'students': 600``

Here is the output when we use the ``len()`` function.

.. code-block:: 

    >>> len(class_dict)
    4

We are assured that the ``len()`` function accurately returns the number of key-value pairs in ``class_dict``.