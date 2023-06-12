Writing Boolean Expressions
===========================

Let's use what we've learned so far to create a boolean expression according to a specification we give you.

We have provided a part of a Python program below that declares the variable ``number_of_work_hours`` and ``number_of_paid_hours``.

Add a new declaration for a variable named ``is_enough_time`` that stores a boolean value (``True`` or ``False``) determining if ``number_of_work_hours`` is less than or equal to ``number_of_paid_hours``.

At the end of your program, it should print ``is_enough_time``. (The code for printing this is already provided)

**Tips**

* Remember the boolean expressions we have learned (``==``, ``<``, ``>``, <=, >=, ``and``, ``or``)

**Sample Input 1:**

``8
10``

**Sample Output 1:**

``True``

**Sample Input 2:**

``22
22``

**Sample Output 2:**

``True``

**Sample Input 3:**

``10
9``

**Sample Output 3:**

``False``

.. challenge::
    :tester: /_static/cs515_challenges/Week1/Challenge15/test_work.py

    number_of_work_hours = int(input())
    number_of_paid_hours = int(input())

    # add the declaration of is_enough_time here

    print(is_enough_time)