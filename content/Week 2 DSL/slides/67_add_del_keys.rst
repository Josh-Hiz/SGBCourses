Adding and deleting keys
========================

There are many circumstances in which we may want to modify a dictionary that has already been created by adding or deleting **key-value pairs**. We will reference the same example dictionary ``class_dict`` in the following sections.

.. code-block:: 

    class_dict = {'instructors': 2, 'TAs': 10, 'tutors': 35, 'students': 600}

Adding Key-Value Pairs
----------------------

We can add a **key-value** pair to an existing dictionary with the syntax:

``dictionary[key] = value``. Let's add a new **key-value pair** to the example dictionary from above.

.. code-block:: 

    class_dict["head tutors"] = 3

Now, calling ``print(class_dict)`` will display this:

.. code-block:: 

    {'instructors': 2, 'TAs': 10, 'tutors': 35, 'students': 600, 'head tutors': 3}

Deleting Key-Value Pairs
------------------------

We can delete **key-value pairs** from a dictionary with a little help from the ``del`` keyword. To delete the ``'head tutors': 3`` **key-value pair** we just added, we can run the line ``del class_dict["head tutors"]``. Then, calling ``print(class_dict)`` will display this:

.. code-block:: 

    {'instructors': 2, 'TAs': 10, 'tutors': 35, 'students': 600}
