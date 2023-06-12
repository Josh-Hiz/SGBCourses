Excuse me, this is a library
============================

Another string method is ``isupper``, and is documented as follows:

    str.isupper()

    Returns True if the string is at least one character long and all cased characters are uppercase

Example usage:

.. code-block:: 

    >>> all_upper = "HELLO!"
    >>> all_upper.isupper()
    True
    >>> not_all_upper = "Hello!"
    >>> not_all_upper.isupper()
    False

For this challenge, define a function called ``quieter_please`` that takes in one string argument and checks if the string is all uppercase. If it is all upper case, convert the string to all lowercase and return this lowercased string. If the argument string is not all uppercase, return this same string, unmodified.

**Note:** In Step 1, we learned about the ``upper()`` method, which produces a new string with all letters converted to uppercase. There is also a ``lower()`` method, which will produce a new string with all letters converted to *lowercase*.

**Sample Input 1:**

.. code-block::
    
    MAKE ME LOWERCASE, PLEASE!

**Sample Output 1:**

.. code-block::
    
    make me lowercase, please!

**Sample Input 2:**

.. code-block::
    
    i'm already lowercase

**Sample Output 2:**

.. code-block::
    
    i'm already lowercase

**Sample Input 3:**

.. code-block::
    
    I have both UPPERcase and lowercase

**Sample Output 3:**

.. code-block::
    
    I have both UPPERcase and lowercase

.. challenge:: 
    :tester: /_static/cs515_challenges/Week2/Challenge9/test_task.py

    # define quieter_please
