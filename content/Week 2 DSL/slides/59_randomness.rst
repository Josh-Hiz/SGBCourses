Randomness
==========

Finally, Python has many useful *modules* that we can use. Specially in this lesson, we will learn how to **import** and use the **random** module to randomly choose an integer within a bound. You'll need this for the challenge problems this week.

To begin using any modules, you will need an ``import`` statement to load the module. All ``import`` statements should be at the beginning of your Python file. In this case, you will need to add the statement ``import random`` at the beginning of your Python file to load the definitions from the ``random`` module. You can access the definitions by writing ``random.<NAME>``.

To randomly choose a number within a bound, you can use ``random.randint(start,end)`` which returns some randomly picked integer ``N`` where ``start <= N`` and ``N <= end``, i.e., inclusive on both.

Below is an example of importing and using ``random.randint()``. Notice that the first statement is ``import random``. Since we provided the bounds 1 and 10 to r``andom.randint()``, ``random_num`` will be any number between 1 to 10. Try running this code multiple times to confirm that different numbers between 1 and 10 are printed each time.

.. runner:: 

    import random
    random_num = random.randint(1, 10)
    print(random_num)