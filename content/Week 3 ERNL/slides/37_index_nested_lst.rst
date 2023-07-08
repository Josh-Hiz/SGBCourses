Indexing nested lists
=====================

Let's return to our earlier example, where we have the variables:

.. code-block::

    student1 = [100,80,95,84]
    student2 = [68,99,70,95]
    student3 = [40,100,95,80]
    student4 = [65,70,68,80]
    student5 = [70,79,85,96]

    grades = [student1,student2,student3,student4,student5]

Now, let's cut out the middleman and create the list ``grades_2D`` without using variables as intermediaries, like in the previous step. We would have:

.. code-block::

    grades_2D = [[100,80, 95, 84],
                 [68, 99, 70, 95],
                 [40, 100,95, 80],
                 [65, 70, 68, 80],
                 [70, 79, 85, 96]]

Note that ``grades_2D`` and ``grades`` are completely identical lists for all practical intents and purposes. Now, say we want to access a particular student's grades from ``grades_2D``. We can do this quite easily using indexing. To get the first student's grades, we can use ``grades_2D[0]``, which will give us ``[100,80,95,84]``. Now, say we want to print a particular student's grade on a specific exam. How might we go about printing, say, the 3rd student's grade on the 4th exam? First, let's start by getting the 3rd student's list of grades and storing it in a temporary variable. Remember, indices start at 0, so the xth student's grades will be at index *x - 1*.

``temp = grades_2D[2]``

``temp`` now contains the list of student 3's grades. Note, ``temp`` is now completely identical to the list ``student3`` we defined at the top of this lesson. Now, we can access the index of the 4th exam from this ``temp`` variable.

``print(temp[3])``

This will print out ``80``. This solution works, and is fairly intuitive. However, it is a little tiresome (and potentially confusing) to have to create a temporary variable every time we want to access an individual element from this **list of lists** (aka **2D list**). Thankfully, Python makes it easy for us to get elements from a **2D list**. We can simply use ``grades_2D[2][3]`` to retrieve the item at index **3** in the list at index **2** in our **list of lists**, ``grades_2D``. Let's get some more practicing with this indexing.