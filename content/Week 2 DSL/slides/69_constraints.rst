Constraints on dictionary keys
==============================

Key Uniqueness and Updating Key-Value Pairs
-------------------------------------------

While dictionaries are very flexible and useful tools, there are some things we must keep in mind when working with them. The first is **key uniqueness**. Simply put, all keys in a dictionary must be unique. You cannot have two identical keys in a dictionary. Let's take a look at an example for a different class.

.. code-block:: 

    class_dict = {'instructors': 2, 'TAs': 10, 'tutors': 35, 'students': 600, 'instructors': 5}

What happens when we inspect the content of this dictionary with a call to ``print(class_dict)``? We get:

.. code-block:: 

    {'instructors': 5, 'TAs': 10, 'tutors': 35, 'students': 600}

As you can see, only the second **key-value assignment** of ``'instructors' : 5`` remains in the dictionary. Similarly, if we were to run the line ``class_dict['instructors'] = 7`` after, the dictionary would then be:

.. code-block:: 

    {'instructors': 7, 'TAs': 10, 'tutors': 35, 'students': 600}

Any **value** assignment to an existing **key** will overwrite the existing **value** associated with said **key**, not create a new **key-value pair**.

This process is referred to as **updating** a **key-value pair**.

**Updating Key-Value Pairs**
----------------------------

We can update an existing pair with the same syntax as adding a pair, using ``dictionary[key] = value``. For example, after changing the value associated with key ``'instructors'``, if we want to change the **value** associated with the **key** ``'TAs'`` to 5, we can run the line ``class_dict['TAs'] = 5``. Then, calling ``print(class_dict)`` would display:

.. code-block:: 

    {'instructors': 7, 'TAs': 5, 'tutors': 35, 'students': 600}

**Value Uniqueness?**
---------------------

While it is impossible to have duplicate **keys**, there is no restriction on duplicate **values**. You may have as many duplicate **values** as you please. For example,

.. code-block:: 

    class_dict = {'instructors': 1, 'TAs': 1, 'tutors': 1, 'students': 1}

is a perfectly valid dictionary (but a pretty weird class).

Key Immutability
----------------

Keys need not be strings, but they should be some **immutable** datatype. This means keys can be **integers**, **strings**, or even **tuples**, but not lists or other dictionaries. Keep in mind though, **values** can be anything (including **lists**, **dicts**, and other mutable datatypes).