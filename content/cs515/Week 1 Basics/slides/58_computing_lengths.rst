Computing the Lengths of Strings
================================

Recall that strings are a datatype for storing text and can be created by writing some characters in between single or double quotes:

.. code-block:: python

    >>> "CS 515-A"
    'CS 515-A'
    >>> 'CS 515-A'
    'CS 515-A'

In this lesson, you will be learning more ways to use strings. In Python, you can think of strings as sequences of characters and the length of a string is the number of characters. To compute the length of a string, you can use the len() function. You can pass the len() function a string value (or a variable containing a string), and the function evaluates the number of characters in that string. 

.. code-block:: python

    >>> len("hello")
    5
    >>> s1 = 'CS 515-A!'
    >>> len(s1)
    9
    >>> len('')
    0

The string '' contains no characters and is called an (or "the") empty string.

