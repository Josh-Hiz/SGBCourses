Lists of lists
==============

Suppose we are in charge of tallying up a class of five student's grades on four exams, then printing out a report for each of them. We might start by creating a list for each student like so:

.. code-block::

    student1 = [100,80,95,84]
    student2 = [68,99,70,95]
    student3 = [40,100,95,80]
    student4 = [65,70,68,80]
    student5 = [70,79,85,96]

However, now, we have a problem. We need a way to print out a report for each of the five students. We can do that, but it's quite tedious. We could try something along the lines of:

.. code-block::

    print("Student 1's Grades: ")
    for exam_no in range(len(student1)):
        print("Exam " + str(exam_no + 1) + ": " + str(student1[exam_no]))

    print("Student 2's Grades: ")
    for exam_no in range(len(student2)):
        print("Exam " + str(exam_no + 1) + ": " + str(student2[exam_no]))

    # repeat for all five students  . . .

Which will output :

.. code-block::

    Student 1's Grades: 
    Exam 1: 100
    Exam 2: 80
    Exam 3: 95
    Exam 4: 84

    Student 2's Grades: 
    Exam 1: 68
    Exam 2: 99
    Exam 3: 70
    Exam 4: 95

    # and so on . . .

This works, but it is very repetitive and tedious to type. Furthermore, it's a very inflexible solution. While we can add more grades on for each student easily by using the ``.append()`` method, we cannot easily add more students to the class without adding many lines of code. Furthermore, it should be very obvious why using this method with a class of 100 students would be very, very difficult to do using this method. 

So now, let's think of a solution. We have repetitive code blocks that we want to remove, and we now know we can nest for loops. But what do we iterate over? We want to print the report for each student variable. Let's make a list out of these lists like this:

``grades = [student1,student2,student3,student4,student5]``

We now have a list created from the variables we defined at the top of this lesson, each of which contains a list. We can now iterate over the list of lists, then iterate over each list individually. This can be difficult to conceptualize initially, so let's go through some examples to see exactly how this **list of lists**, or **2D list**, works.

.. code-block::

    for lst in grades:
        print(lst)

What will be printed when you run this? It will be each of the lists in ``grades``. We can now take advantage of the code snippet we defined above to print a report on each student using a single code block in a nested for loop, like this:

.. code-block::

    for lst in grades:
        print("Student's Grades: ")
        for exam_no in range(len(lst)):
            print("Exam " + str(exam_no + 1) + ": " + str(student1[exam_no]))

The first for loop ``for lst in grades`` iterates over the list of lists, then the second for loop ``for exam_no in range(len(lst))`` iterates over the individual grades in each student's list of grades, printing them out as above. Let's get a little practice with iterating over **2D lists**.