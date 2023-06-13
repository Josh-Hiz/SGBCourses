List methods
============

Append
------

.. code-block:: 

    lst.append(elem)

Adds the specified element (elem) to the end of the list

.. code-block:: 

    >>> l = [1, 2, 3, 4, 5]
    >>> l.append(0)
    >>> l
    [1, 2, 3, 4, 5, 0]

The append method in the above example added the element 0 to the end of the list.

Index
-----

.. code-block:: 

    lst.index(elem)

Returns the position of the first occurrence of the specified element (elem).

.. code-block:: 

    >>> l = [1,2,3,4,5,3,3]
    >>> l.index(3)
    2

The index method in the above example returned the index of the first occurrence of the element 3 which is 2 in zero-based indexing.

Insert
------

.. code-block:: 

    lst.insert(pos, elem)

Inserts the specified element (elem) at the specified position (pos)

.. code-block:: 

    >>> l = [1,2,3,4,5]
    >>> l.insert(3, 0)
    >>> l
    [1, 2, 3, 0, 4, 5]

The insert method in the above example inserted the element 0 at the index 3 (zero-based indexing) and thus the list now contains the element 0 at the index 3.

Pop
---

.. code-block:: 

    lst.pop(pos)

Removes and returns the element at the specified position. The pos parameter is optional. If it is not specified then the default value of pos is -1 and it removes the last element

.. code-block:: 

    >>> l = [1,2,3,4,5]
    >>> l.pop(3)
    4
    >>> l
    [1, 2, 3, 5]
    >>> l.pop()
    5
    >>> l
    [1, 2, 3]

In the first example, the pop method is used with a parameter that specifies the index at which the element needs to be removed. So in the first example, pop method removed and returned the element at index 3 (zero-based indexing) which is 4. In the second example, when no parameter is given to the pop method, it removes and returns the last element in the list.

Reverse
-------

.. code-block:: 

    lst.reverse()

Reverses the order of the elements in the list. Note that it doesn't return anything---it just modifies the list *in place*.

.. code-block:: 

    >>> l = [4,7,2,0,9]
    >>> l.reverse()
    >>> l
    [9, 0, 2, 7, 4]

The reverse method in the above example reversed the order of the elements in the given list.