Hardened square-root program
============================

Write a program that takes a floating point number as user input. It then uses ``math.sqrt`` to take the square root and print it out.

Your program should: 

* not catch ``^C``
* not throw any exceptions when given a non-float input
* not throw any exceptions when given a negative number
* not complete until its received a valid input

Here are three sample interactions, with user input in **bold**:

.. code-block:: 

    $ python task.py
    Enter a floating point number: 25
    The square root of 25.0 is 5.0.

.. code-block::

    $ python task.py
    Enter a floating point number: lol
    'lol' is not a floating point number.
    Enter a floating point number: -1
    '-1.0' doesn't have a (real) square root.
    Enter a floating point number: 10.0
    The square root of 10.0 is 3.1622776601683795.

.. code-block:: 

    $ python task.py
    Enter a floating point number: ^CTraceback (most recent call last):
        File "/home/task.py", line 7, in <module>
            s = input('Enter a floating point number: ')
    KeyboardInterrupt

Hint: you may need to use both ``try``/ ``except`` and ``if`` to handle and detect error conditions. Tricky business!

.. challenge:: 
    :tester: /_static/cs515_challenges/Week3/Challenge1/test_task.py

    # you need this line to get math.sqrt
    import math

    # read a float from the user and print out its square root