Counting needles in a haystack
==============================

Write a function called ``count_str(string, s)`` that takes two parameters. The first parameter is the string ``str`` and the second parameter is another string ``s``. You need to use the ``count`` method to count the number of times the string ``s`` appears in the string ``string`` and return that ``count`` value.

(An earlier version of this challenge used ``str`` as the name of the first parameter... that's a terrible idea, because ``str`` is also the name of the global type of strings, and using it as a variable name will shadow the global type. Similarly, you should avoid naming things ``int`` or ``float`` or ``list``.)

**Sample Input 1:**

.. code-block:: 
    
    banana
    a

**Sample Output 1:**

.. code-block:: 

    3

**Sample Input 2:**

.. code-block::

    banana
    n

**Sample Output 2:**

.. code-block::

    2

**Sample Input 3:**

.. code-block::

    a
    z

**Sample Output 3:**

.. code-block::

    0

.. challenge:: 
    :tester: /_static/cs515_challenges/Week2/Challenge8/test_task.py

    # define count_str