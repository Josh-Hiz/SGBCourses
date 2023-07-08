Making a 2D list
================

To create a 2D list, we simply create a list as normal, then insert more lists as elements in the first list. It is convention to use newlines to make your 2D list look nice and readable for the purposes we suggested in the prior step, but its not necessary. As a very basic example, here is a 2D list, which is simply a list of three identical lists with two integers in them.

.. code-block::

    empty_2D = [[0,1],
                [0,1],
                [0,1]]

Here, we use newlines to make the list look pretty, but we can also write ``empty_2D`` like so:

.. code-block::

    empty_2D = [[0,1],[0,1],[0,1]]

These two versions of ``empty_2D`` are completely identical. In programming terms, we might call the first version of the list **syntactic sugar**. This just means doing something that isn't strictly necessary that makes the program easier, or "sweeter", for programmers to read and use.

We can use for loops on 2D lists extremely easily as well. Remember, when we iterate over a list, such as ``lst = ['a','b','c']`` using a loop such as ``for element in lst``, we iterate over each individual **element** of the list. When we work with 2D lists, this works exactly the same way, except that each **element is a list**! 

Now, let's get some practice creating our own 2D lists. We will run the following for loop on your 2D list, defined in the variable ``list_2D``.

.. code-block::

    for lst in list_2D:
        print(lst)

Create a 2D list so that the output is the same as the test case! Remember, when we iterate over a **2D list** like ``list_2D``, each element will be a list. Note: there is no input for this code challenge. Only ``list_2D`` will be considered.

**Desired output:**

.. code-block::

    [1, 2, 3]
    [4, 5, 6]
    [7, 8, 9]

.. challenge::
    :tester: /_static/cs515_challenges/Week3/Challenge7/test_task.py

    # define list_2D (we'll write the loop)