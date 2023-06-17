Using methods for lookup
=========================

We've learned in previous lessons that values in dictionaries can be accessed by including the corresponding keys between brackets ``[]``. Let's bring back our example ``class_dict`` and read its contents.

.. code-block:: 

    class_dict = {'instructors': 2, 'TAs': 10, 'tutors': 35, 'students': 600}

If the number of instructors in the class is inquired, for instance, then the number can be accessed by the following:

.. code-block:: 

    >>> class_dict['instructors']
    2

What happens if your code tries to access a key not included in the dictonary? It results in an error.

.. code-block:: 

    >>> class_dict['pets']
    Traceback (most recent call last):
    File "<pyshell#21>", line 1, in <module>
        class_dict['pets']
    KeyError: 'pets'

The dictionary method ``get()`` can access dictionaries in a similar fashion except that it does not result in *KeyError*. When one wants to read the value that corresponds to a specific key in a dictionary, the method ``get()`` can be used in the format of ``dictionary.get(key)``. If the number of instructors in the class is asked again, then the result can be returned as follows, which will have the same effect as ``class_dict['instructors']``.

.. code-block:: 

    >>> class_dict.get('instructors')
    2

However, when we try to access a key that does not exist, nothing is returned and the next prompt shows up right away.

.. code-block::

    >>> class_dict.get('pets')
    >>>

This is different from the previous way because it does not crash with *KeyError*. What actually happens is that the ``get()`` method returns ``None``. We can confirm this by printing it out.

.. code-block:: 

    >>> print(class_dict.get('pets'))
    None

Since it's preferable to avoid exceptional control flow, the ``get`` method is a good choice when you're not sure if the key is in the map. One wrinkle: it's hard to tell the difference between an absent key and a key mapping to the value ``None``!

Get with a default
------------------

You can also call the ``get`` method with a default, as in:

.. runner::

    d = { 'greeting': 'hi' }
    print(d.get('greeting', 'hello'))
    print(d.get('farewell', 'goodbye'))
    d['farewell'] = 'hasta luego'
    print(d.get('farewell', 'goodbye'))