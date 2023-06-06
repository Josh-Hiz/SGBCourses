Indexing
========

When working with strings, it is very helpful to be able to extract a character from a specific position. We will refer to positions as **indexes**. The first position will be the 0th index and will increase by 1 for each next position. This concept is called **0th base indexing**.

Given a string "CS 515-A!", the following table shows the corresponding index of each character. Notice that the first character 'C' is in index 0, the last character '!' is in index 8, and the length of the string is 9.

.. code-block::

    character: C S   5 1 5 - A !
        index: 0 1 2 3 4 5 6 7 8

To retrieve a character from a specific index, you can use the **bracket lookup expression**. This expression is denoted by square brackets next to the string or variable with a string. Within the square brackets, you will have to provide the index you want to retrieve a character from. This is called **indexing**. Indexes can be only integer values, not floats.

**Index Out of Bounds**

Now you may be wondering what happens if you provide an index not within the range of indexes (or indices). Python will give you an IndexError error message if you try to index a number beyond the range of indexes for a particular string. The example below shows the error message for an ``IndexError``. We will sometimes refer to this error as **index out of bounds** or **index out of range**.

.. code-block:: 

    >>> course = "CS 515-A!"
    >>> course[9]
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    IndexError: string index out of range

Note that in the above example, the first character 'C' is at index 0 and the last character '!' is at index 8. Therefore, accessing the character at index 9 (which does not exist) will result in an index out of bounds error.

**Negative Indexes**

While indexes start at 0 and go up, you can also provide negative integers for the index. The integer value -1 refers to the last index in a string, the value -2 refers to the second-to-last index in a string, and so on.

Given a string "CS 515-A!", the following table represents the index of each character using **negative indexes**. Since '!" is the last character, the negative index is -1 and 'C' is the last character backwards so it is in index -9. 

**The Last Element**

The last index of a string is always the length of the string minus 1. There are two ways to obtain the last character of a string. You can either use the index ``-1`` or use the ``len()`` function and subtract 1 from it.

.. code-block:: python

    >>> course = "CS 515-A!"
    >>> course[len(course)-1]
    '!'
    >>> course[-1]
    '!'
