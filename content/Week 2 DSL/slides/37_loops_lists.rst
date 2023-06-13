Using for loops with lists
==========================

As you are aware by now, a for loop iterates over iterable things---and lists are iterable! 

An example of a for loop iterating over a list:

.. runner:: 

    for x in [5, 2, 3, 1]:
        print(x)

In this example, the first time the body of the loop is evaluated, x has a value equal to the first element in the list (i.e., element at index 0), which is 5.

* First iteration: ``x`` has a value of 5, the body of the loop is evaluated with this value of ``x``

* Second iteration: ``x`` has a value of the next member in the sequence, 2, and the body of the loop is evaluated with this value of ``x``

* Third iteration: ``x`` has a value of the next member in the sequence, 3, and the body of the loop is evaluated with this value of ``x``

* Fourth iteration: ``x`` has a value of the next member in the sequence, 1, and the body of the loop is evaluated with this value of ``x``

* Since there are no more members to iterate over in the sequence of members, the for loop is done being evaluated

This loop would print:

.. code-block:: 

    5
    2
    3
    1

Similarly, if we want to find the sum of all elements inside a list, then we can use a for loop to achieve it as follows:

.. runner:: 

    lst = [13, 12, 17, 19, 33, 0]

    sum_of_elements = 0
    for elem in lst:
        sum_of_elements = sum_of_elements + elem

    print(sum_of_elements)

This for loop iterates over each element in the list and adds it to the variable sum_of_elements which holds the total sum of all the elements in the list. The output of the above code snippet is:

.. code-block:: 

    94