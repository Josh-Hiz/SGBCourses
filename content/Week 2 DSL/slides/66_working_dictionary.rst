Working with dictionaries
=========================

Printing Dictionaries
---------------------

Although dictionaries are a new data structure, we can still use a lot of Python knowledge we already have to get the most out of them. Dictionaries work just fine with ``print()``, and we can use the ``print()`` function on dictionaries to easily check their contents. We can simply call ``print()`` on a dictionary the same way we do for ``int``, ``string``, or ``list`` datatypes. Here's an example with the dictionary from the previous steps.

.. code-block:: 

    class_dict = {'instructors': 1, 'CAs': 2, 'students': 59}

If we run ``print(class_dict)``, we would get the output:

.. code-block:: 

    {'instructors': 1, 'CAs': 2, 'students': 59}

Note that dictionaries are enclosed by curly braces ``{}`` when being printed. 

Iterating over Dictionaries with a For Loop
-------------------------------------------

We can use for loops on dictionaries in a very similar way to lists. Using a for loop over a dictionary will iterate over the **keys** of the dictionary. Let's use a for loop to print all the **keys** in ``class_dict``.

.. code-block:: 

    for key in class_dict:
        print(key)

The above code would output:

.. code-block:: 

    instructors
    CAs
    students

Note: As of Python 3.5, the order of items in a dictionary will be consistent. Since we defined class dict in the order ``instructors``, ``CAs``, ``students``, that is the order they will be iterated over in the for loop. However, in older versions of Python, the order will be arbitrary, so be careful. In Python 2.6 for example, the order could be any combination of ``instructors``, ``CAs``, ``students``, and we wouldn't know until we ran the loop.

Say we want to print all **key : value** pairs in a dictionary. How will we go about that? We can do a loop like this:

.. code-block:: 

    for key in class_dict:
        print(key + " : " + str(class_dict[key]))

Try it for yourself and observe the output.

Using the "in" Operator
-----------------------

Similar to how we can use the ``in`` operator to check for list membership, we can also use the same ``in`` operator to check if a particular **key** is in a dictionary. For example, the following line:

.. code-block:: 

    "CAs" in class_dict

evaluates to ``True``.

Similarly,

.. code-block::

    "vuvuzelas" in class_dict

evaluates to ``False``.

Note that the ``in`` operator on a dictionary will only check for **keys**, not **values**. So,

.. code-block:: 

    "vuvuzelas" in class_dict

evaluates to ``False``.

Note that the ``in`` operator on a dictionary will only check for **keys**, not **values**. So,

.. code-block:: 

    2 in class_dict

will evaluate to ``False``, even though ``2`` is a **value** in the dictionary associated with the **key** ``"CAs"``.