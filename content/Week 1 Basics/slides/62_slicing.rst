Slicing
=======

So far you've learned how to obtain a character at a specific index. In Python, you can get a subsection of a string by slicing. This is useful if you only want part of the string. **Slicing** is done by using the ``:`` operator inside square brackets. The integer in front of the ``:`` operator is the starting index (inclusive) and the integer after the : operator is the ending index (exclusive). The resulting string is commonly referred to as a substring and will not include the character at the ending index. A **substring** is any sub portion of a string.

.. code-block:: python

    >>> "hello world"[0:5]
    'hello'

Since the starting index is 0 and the ending index is 5, our resulting substring contains the characters from indexes 0 to 4 since slicing does not include the character from the ending index.

.. code-block:: python

    >>> "hello world"[6:11]
    'world'

Similar to indexing, the indexes provided have to be within the range of the string. Notice that 11 is not an index within the range for the string "hello world". However, this did not cause an error because slicing does not look for the character in the ending index. Thus, we have the substring "world" which contains the characters in indexes 6 to 10.
