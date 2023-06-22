I Am Very Excited!!!!!!!
========================

Write a function ``exclaim`` that takes a string and a integer, and produces that string with a number of exclamation marks after it equal to the given integer. You only need to consider cases where the number is 0 or greater (no negative numbers).

For example, ``exclaim("Hey", 4)`` should produce ``"Hey!!!!"``

Hint: An interesting trick with Python strings is that you can *multiply* a string by a number to replicate the string that many times. For example:

.. code-block:: python

    >>> "na" * 4
    'nananana'

**Sample Input 1:**

.. code-block::

    Hey 4

**Sample Output 1:**

.. code-block::
    
    Hey!!!!

**Sample Input 2:**

.. code-block::

    Hey 0

**Sample Output 2:**

.. code-block::
    
    Hey

**Sample Input 3:**

.. code-block::

    ! 2

**Sample Output 3:**

.. code-block::
    
    !!!

**Sample Input 4:**

.. code-block::

    Ah 1

**Sample Output 4:**

.. code-block::
    
    Ah!

.. challenge::
    :tester: /_static/cs515_challenges/Week1/Challenge14/test_exclaim.py
