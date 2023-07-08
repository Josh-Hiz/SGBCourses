Iterate through lists using inner for-loops
===========================================

We've already seen nested for-loops in which we iterate through a list using the inner for-loop:

.. code-block::

    for i in range(n):
        for j in range(len(cases)):
            print(cases[j])

This is the code the researcher's friend provided to print multiple copies of elements in ``cases``.

Notice that the **outer for-loop** is just to repeat our **inner for-loop** for ``n`` times, while the **inner for-loop** is the one that iterates through **cases** and prints out the elements.

Iterate through lists using outer for-loops
-------------------------------------------

We can also use the **outer for-loop** to iterate through a list, and do something with each element in the list using the **inner for-loop**!

Consider the following example code snippet:

.. runner::

    lst = [1, 2, 3, 4]
    for n in lst:
        factorial = 1
        for j in range(1, n + 1):
            factorial *= j
        print('Factorial of the element at index ' + str(n) + ' is: ' + str(factorial))

The code above uses a nested for-loop, and it will calculate the factorial of each element in ``lst`` and print it out.

The code above uses a nested for-loop, and it will calculate the factorial of each element in ``lst`` and print it out. The output is:

.. code-block::

    Factorial of the element at index 1 is: 1
    Factorial of the element at index 2 is: 2
    Factorial of the element at index 3 is: 6
    Factorial of the element at index 4 is: 24

The following snippet shows how the loop gets unrolled to reach the above output. Notice how the number of iterations of the inner loop is dependent on the value of ``n``, the elements of the list being traversed using the outer for-loop.

.. code-block::

    #In the 1st iteration:

    n = 1
    factorial = 1 #factorial is set to 1
    #The inner for loop equivalently becomes:
    for j in range(1, 2):
        factorial *= j
    #The inner loop gets executed once and we get factorial = 1


    #In the 2nd iteration:

    n = 2
    factorial = 1 #factorial is reset to 1
    #The inner for loop equivalently becomes:
    for j in range(1, 3):
        factorial *= j
    #The inner loop gets executed twice and we get factorial = 1*2 = 2



    #In the 3rd iteration:

    n = 3
    factorial = 1 #factorial is reset to 1
    #The inner for loop equivalently becomes:
    for j in range(1, 4):
        factorial *= j
    #The inner loop gets executed thrice and we get factorial = 1*2*3 = 6


    #In the 4th iteration:

    n = 4
    factorial = 1 #factorial is reset to 1
    #The inner for loop equivalently becomes:
    for j in range(1, 5):
        factorial *= j
    #The inner loop gets executed four times and we get factorial = 1*2*3*4 = 24

Iterate through lists using both outer for-loops and inner for-loops?
---------------------------------------------------------------------

In fact, as you may probably guess, we can iterate through a list using the **outer for-loop** while at the same time iterate through a list using the **inner for-loop**! Since this is just a combination of the two previously discussed ways of using nested for-loops, we won't get into it here. How about you try some exercises on it yourself?