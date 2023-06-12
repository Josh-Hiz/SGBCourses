References, Objects, and Aliasing
=================================

Two References Pointing to Two Separate Objects
------------------------------------------------

In this example, we have created two lists, ``list1`` and ``list2``. Since the two lists are created separately, ``list1`` and ``list2`` contain separate references to two different lists. Although the values in the list are the same, their memory addresses are different.

.. code-block:: python

    list1 = [1, 2, 3]

    list2 = [1, 2, 3]

    list1[0] = 5

    print("list1 =", list1)
    print("list2 =", list2)

The above code prints the following. Notice that changing the value at index 0 for ``list1`` only changed ``list1``'s list object. This shows that ``list1`` and ``list2`` contain references to separate objects.

.. code-block:: python

    list1 = [5, 2, 3]
    list2 = [1, 2, 3]

Two References Pointing to the Same Object
------------------------------------------

The following is an example of two references pointing to the same object---these are *aliased* references. (An 'alias' is another name for something, from the Latin word *alius*, meaning "other".) The first line creates the list object and ``list1`` now stores the reference to the newly created list object. The second line copies ``list1``'s reference and stores it into ``list2``. In this case, ``list1`` and ``list2``'s references are pointing to the same object.

.. code-block:: python

    list1 = [1, 2, 3]
    list2 = list1

    print("Before modification...")
    print("list1 =", list1)
    print("list2 =", list2)

    list2[0] = 5

    print("After modification...")
    print("list1 =", list1)
    print("list2 =", list2)

The above code prints the following. When we update the value at index 0 for ``list2``, notice that ``list1`` has also been updated. This happened because ``list1`` and ``list2`` contain references to the same list object. Try this out in IDLE and modify the elements in ``list1`` and ``list2``. What happened? Are the two lists always the same?

.. code-block:: 

    Before modification...
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    After modification...
    list1 = [5, 2, 3]
    list2 = [5, 2, 3]