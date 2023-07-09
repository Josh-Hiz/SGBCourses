Nested for loops and 2D lists
=============================

We can quite easily use nested for loops to work with 2D lists in a straightforward manner. Suppose we want to write some code that will print the sum of all integers in a 2D list. How might we go about it? First, let's brush up on how we'd accomplish this with a 1D list.

.. runner::

    lst = [1,2,3,4]
    total = 0
    for idx in range(len(lst)):
        total += lst[idx]

    print(total)

This sort of code should look pretty familiar to you. If you need a refresher, take a look at week 5 in this course. We can use our ``i`` and ``j`` based, row-column system to traverse 2D lists in a similar way. The following code will print the sum of all integers in a 2D list. Keep in mind, ``i`` iterates over the **rows** of this 2D list, while ``j`` iterates over the **columns**. Of course, we can also think of this as ``i`` iterates over the lists inside the list of lists, while ``j`` iterates over the individual elements of each inner list. Notice that these nested loops will iterate over every possible combination of ``i`` and ``j``. To understand why, you may want to copy the following code to a workspace, and add some print statements to take a look at how the values of ``i`` and ``j`` change over the course of the loops being run.

.. runner::

    list_2D = [[0,1,2],
               [3,4,5],
               [6,7,8]]

    total = 0
    for i in range(len(list_2D)):
        for j in range(len(list_2D[i])):
            total += list_2D[i][j]

    print(total)

Of course, we can also use for loops to iterate over items of a list directly, though this may make some tasks more difficult or impossible. This works just fine for this particular task though, as you can see.

.. runner::

    list_2D = [[0,1,2],
               [3,4,5],
               [6,7,8]]
    total = 0

    for lst in list_2D:
        for element in lst:
            total += element

    print(total)

Nested for loops lend themselves perfectly to working with 2D arrays. 