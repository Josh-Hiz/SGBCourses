Slicing Lists
=============

You have learnt how to access a single element from a list. If you want to access a range of elements from a list then we can use the slicing operator ``:`` in order to achieve this. You can specify an integer before and after the slicing operator. The integer before the slicing operator indicates where to start the slice and the integer that comes after indicates where to stop the slice (that stop position not included in the slice). These slices can also be called as sublists.

.. code-block::

    >>> shopping_list = ["milk", "eggs", "bread", "apples", "bananas"]
    >>> shopping_list[1:3]
    ['eggs', 'bread']

Here, the elements of the list starting from index 1 until index 3 are printed out (Notice that the element at index 3 is not included in the slice)

.. code-block::

    >>> shopping_list[0:len(shopping_list)]
    ['milk', 'eggs', 'bread', 'apples', 'bananas']

This slice includes all the elements in the list. Note that ``len(shopping_list)`` will be 5 in the above example. 

.. code-block::

    >>> shopping_list[-3:-1]
    ['bread', 'apples']

Here, the elements of the list starting from index -3 (which is the third to last element of the list) until index -1 (which is the last element of the list) are printed out. (Notice that the element at index -1 is not included in the slice; i.e., the first index of the slice is *inclusive* but the second index is *exclusive*.)

.. code-block::

    >>> shopping_list[1:-2]
    ['eggs', 'bread']

Try to understand why this is the output for the given slice... but maybe don't write code this way if you can avoid it?

Skipping Indices
----------------

As you can see in the above examples, you can use either positive or negative integers or a combination of them as the slice indices which is very similar to what we used as the list indices for accessing the list elements.

You can also choose to not mention either of the starting or the ending integers while creating the slice or the sublist.

.. code-block::

    >>> shopping_list[1:]
    ['eggs', 'bread', 'apples', 'bananas']

Here, the elements of the list starting from index 1 until the end are printed out. If we don't mention the end index in a slice it will default to the length of the list.

.. code-block::

    >>> shopping_list[:-1]
    ['milk', 'eggs', 'bread', 'apples']

Here, the elements from the beginning until index -1 are printed out. (Notice that the element at index -1 is not included in the slice.) If we don't mention the start index in a slice, it will default to 0.