For loops
=========

You learned about lists in the previous module in detail. Now, what if you want to process the data that is stored in a list. One example of this is finding the sum of all the elements in a list – the result of adding them all together.

It turns out there's another whole set of features that will help us solve general challenges in programming with sequences of values: **loops**. Loops' job in programs is to evaluate the same block of code multiple times according to some rules.

for loops
---------

A **for loop** is useful when you want to iterate (i.e., repeat) over a block of code a specific number of times. It iterates over a **sequence**, also known as an **iterable value** or **iterable object**. The syntax of the for statement looks like this:

.. code-block:: 

    for <variable> in <sequence>:
        <body of the for loop>

In this example, <sequence> is an iterable object (e.g., list, string) and the <variable> is a variable name of our choosing. The variable will be set to each value of the sequence one by one in order, and the loop body will run for each one. We call this assignment of the variable and evaluation of the body an **iteration** of the loop. 

The sequence used in a for loop can be generated using a function called ``range()`` which we will discuss in detail. Other examples of a sequences we have already learned are lists and strings.

A concrete example of a for loop using ``range()``:

.. runner:: 

    for x in range(5):
        print("Number " + str(x))

In this example, ``range(5)`` results in five iterations through the code in the body of the loop, with ``x`` being set to 0, then 1, then 2, then 3, and then 4. The end point in a range is never part of the generated sequence. In this example, range(5) generates a sequence with values 0, 1, 2, 3, and 4. The end point (i.e., 5) is not part of the generated sequence.

The first time the body of the loop is evaluated, ``x`` has a value equal to 0. 

* First iteration: ``x`` has a value of 0, the body of the loop is evaluated with this value of ``x``

* Second iteration: ``x`` has a value of the next member in the sequence, 1, and the body of the loop is evaluated with this value of ``x``

* Third iteration: ``x`` has a value of the next member in the sequence, 2, and the body of the loop is evaluated with this value of ``x``

* Fourth iteration: ``x`` has a value of the next member in the sequence, 3, and the body of the loop is evaluated with this value of ``x``

* Fifth iteration: ``x`` has a value of the next member in the sequence, 4, and the body of the loop is evaluated with this value of ``x``

* Since there are no more members to iterate over in the sequence, the for loop is done being evaluated

The above for loop will print the following when executed:

.. code-block:: 

    Number 0
    Number 1
    Number 2
    Number 3
    Number 4