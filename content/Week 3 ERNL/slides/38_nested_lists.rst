Nested lists
============

Let's take another look at our **2D list** ``grades_2D``.

.. code-block::

    grades_2D = [[100,80, 95, 84],
                 [68, 99, 70, 95],
                 [40, 100,95, 80],
                 [65, 70, 68, 80],
                 [70, 79, 85, 96]]

So far, we've been talking about **2D lists** as **lists of lists**, but now let's shift our thinking a little bit so we can work with **2D lists** in a more intuitive manner. We know that we can use two sets of square brackets to access individual elements of this **2D list**, for instance, using ``grades_2D[0][0]`` to get the 0 index item in the 0 index list of ``grades_2D``, which, in this case, is ``100``. While this thinking is strictly correct, it might be helpful to use a more intuitive system to understand this 2D list. Thankfully, there is one! Let's use arbitrary variables ``i`` and ``j`` to index ``grades_2D``. How can we think about ``grades_2D[i][j]``? Take a look at this diagram.

.. image:: /assets/images/cs515/Week3/matrix.png
    :align: center

We can think of ``i`` as the **row** of the **2D list** and of ``j`` as the **column**, just like in an Excel spreadsheet! When we align the elements of the **2D list** like this, it becomes trivial to find the index of a specific element. For example, let's find ``grades_2D[1][2]``. In this case, ``i = 1`` and ``j = 2``. We can mentally do something like:

.. image:: /assets/images/cs515/Week3/matrix2.png
    :align: center

``grades_2D[1][2]`` will be the intersection of those lines, which is 70! Visualizing **2D lists** in this way can be very helpful for accessing and creating them. What elements are at the following indices of ``grades_2D``?

.. free-r::
    :answer: 79

    # Question 1

    What is ```grades_2D[4][1]```?

.. free-r::
    :answer: \s*\[\s*65\s*,\s*70\s*,\s*68\s*,\s*80\s*\]\s*
    :regex: true

    # Question 2

    What is ```grades_2D[3]```?

.. free-r::
    :answer: 80

    # Question 3

    What is ```grades_2D[0][1]```?

.. free-r::
    :answer: .*IndexError.*
    :regex: true

    # Question 4

    What is ```grades_2D[4][4]```?

.. free-r::
    :answer: 65

    # Question 5

    What is ```grades_2D[3][0]```?