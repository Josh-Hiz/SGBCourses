Characterizing Numbers
======================

Write a function ``get_num_type(num)`` that returns the following output based on the value of ``num``. You can assume that ``num`` will always be an integer.

``get_num_type`` should return:

* "zero" if ``num`` is 0
* "positive and odd" if ``num`` is a positive number as well as an odd number
* "positive and even" if ``num`` is a positive number as well as an even number
* "negative and odd" if ``num`` is a negative number as well as an odd number
* "negative and even" if ``num`` is a negative number as well as an even number

**Sample Input:**

.. code-block:: 

   11

**Sample Output:**

.. code-block:: 

   positive and odd

.. challenge::
   :tester: /_static/cs515_challenges/Week1/Challenge18/test_num.py

   # define get_num_type here