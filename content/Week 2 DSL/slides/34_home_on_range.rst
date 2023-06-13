Home on the range
=================

When we want to iterate through a range of values, we take the help of the function ``range()``.

A very basic use of range is to pass an integer argument to range like we saw in the example in the previous reading. Here is an example: ``range(5)``

This returns a sequence of integer values from 0 up until, but not including, the passed value. In the example above, it is a sequence from 0 to 5, not including 5 (i.e., 0, 1, 2, 3, 4).

.. runner:: 

    total_sum = 0
    for i in range(5):
        print('i is ' + str(i))
        total_sum += i    # same as total_sum = total_sum + i
        print('total_sum is ' + str(total_sum))

The above for loop would iterate a total of 5 times

* In the first iteration, ``i`` is equal to 0. After the body of the loop is evaluated, ``total_sum`` has a value of 0.

* In the second iteration, ``i`` is equal to 1. After the body of the loop is evaluated, ``total_sum`` has a value of 1.

* In the third iteration, ``i`` is equal to 2. After the body of the loop is evaluated, ``total_sum`` has a value of 3.

* In the fourth iteration, ``i`` is equal to 3. After the body of the loop is evaluated, ``total_sum`` has a value of 6.

* In the fifth iteration, ``i`` is equal to 4. After the body of the loop is evaluated, ``total_sum`` has a value of 10.

* There are no more values to iterate over in the sequence ``range(5)``, so the loop is done being evaluated.

The resulting value of ``total_sum`` is 10.

Start, stop and step arguments in range()
-----------------------------------------

The ``range()`` function can also be called with two or even three arguments as follows:

.. runner:: 

    for i in range(3, 6):
        print(i)

This would print:

.. code-block:: 

    3
    4
    5

As it is evident from the example above, when ``range()`` is called with two arguments, the first argument or parameter in the ``range()`` function is considered as the *starting point* for the sequence generated and the second argument is considered as the *ending point* (not included in the sequence). (Notice that we're inclusive at the beginning and exclusive at the end---just like for slicing.)

.. runner:: 

    for i in range(3, 10, 3):
        print(i)

This would print:

.. code-block:: 

    3
    6
    9

Along with the starting point and the ending point, we can call ``range()`` with three arguments. The third argument will be the *step* as the third argument to the ``range()`` function. The step is added to the previous number in the sequence in order to get to the next number in the sequence; above, the step value is 3, so we count by threes.

More examples and uses of range can be found here: https://docs.python.org/3/library/stdtypes.html#range