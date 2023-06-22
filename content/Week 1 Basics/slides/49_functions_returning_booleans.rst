Functions Returning Booleans
============================

Write a function called ``is_less_than_10`` that takes an integer and returns a boolean value, ``True`` if the integer is less than ``10``, otherwise False (see the sample inputs for some examples). You can pick everything about the parameter name and how you write the body of the function, but it must be called ``is_less_than_10``.

The code challenge will call your ``is_less_than_10`` function with many inputs and check that it behaves correctly on all of them. You are not required to handle non-integer inputs to your program.

**Sample Input 1:**

.. code-block::

   2

**Sample Output 1:**

.. code-block::

   True

**Sample Input 2:**

.. code-block::

   3

**Sample Output 2:**

.. code-block::

   True

**Sample Input 3:**

.. code-block::

   11

**Sample Output 3:**

.. code-block::

   False

**Sample Input 4:**

.. code-block::

   10

**Sample Output 4:**

.. code-block::

   False

.. challenge::
   :tester: /_static/cs515_challenges/Week1/Challenge16/test_fun.py

   # Define your is_less_than_10 function here: