Operations on Lists
===================

Modifying elements in a list using indices
------------------------------------------

You have learned how to define lists and how to access each element in a list using indices. Using these indices, you can also modify the element present in the list. For example, let us define a list of floating point values as follows:

.. code-block::
    
    >>> wages = [40.25, 51.5, 35.4, 42.34]

Now, if we want to modify the value at index 2 in this list from 35.4 to 38.5 then we can do it as follows:

.. code-block::
    
    >>> wages[2] = 38.5

If you print the list ``wages`` now, then you see that the element at index 2 has been modified.

.. code-block::
    
    >>> wages
    [40.25, 51.5, 38.5, 42.34]

.. code-block::

    [40.25, 51.5, 38.5, 42.34]

List Concatenation and List Replication
---------------------------------------

Similar to Strings, we can perform concatenation of two different lists using the ``+`` operator in order to create a combined list. And if we want to replicate the list a specific number of times then we can use the ``*`` operator along with an integer that represents how many times you want the list to be replicated.

.. code-block::

    >>> new_wages = wages + [39.2, 41.5]
    >>> new_wages
    [40.25, 51.5, 35.4, 42.34, 39.2, 41.5]

.. code-block::

    >>> new_wages

.. code-block::

    [40.25, 51.5, 35.4, 42.34, 39.2, 41.5]

Here, we have combined the list ``wages`` and another list containing two values into a new list ``new_wages`` with the help of the + operator. 

.. code-block::

    >>> replicated_wages = wages * 2
    >>> replicated_wages
    [40.25, 51.5, 35.4, 42.34, 40.25, 51.5, 35.4, 42.34]

Here, we have replicated the elements in the list ``wages`` twice using the ``*`` operator followed by the integer 2.