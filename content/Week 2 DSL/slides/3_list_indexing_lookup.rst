List Indexing and Lookup
========================

We can also access elements of lists individually. The **bracket lookup expression**, a new kind of expression, takes in a number for the **index** of an element to look up. For example:

.. code-block:: 

    >>> some_numbers = [46, 12, 3, 9]
    >>> some_numbers[0]
    46
    >>> some_numbers[1]
    12
    >>> some_numbers[2]
    3

What we might call in English the “first” element, 46, is at what we call **index** 0 in the list (using index 0 got us back 46). This is called **0-based indexing**, and is a common method for indexing in programming languages. It's worth highlighting that len function still reports that this list has 4 elements (it doesn't say 3, counting from 0).

Trying to access an element at an index that's too large raises an error:

.. code-block:: 

    >>> some_numbers[4]
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    IndexError: list index out of range

Trying to access an element at a negative index has a very interesting behavior. When you access the element at index -1, it gives the last element in the list. So we can say that negative indices starting from -1 can be used to access the list starting from the end (like we used positive indices starting from 0 to access the list starting from the beginning of the list).

.. code-block:: 

    >>> some_numbers[-1]
    9
    >>> some_numbers[-2]
    3
    >>> some_numbers[-5]
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    IndexError: list index out of range

**NOTE:** Indexing in **lists** is very similar to indexing in **strings** that we learned previously!