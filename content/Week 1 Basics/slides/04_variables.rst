Variables
=========

There's quite a bit more to say about numbers in programming, but we'll work with what we've seen so far using integers and simple operations for now.

It was useful to use our intuition about math to connect numeric calculation in Python to things we're likely familiar with.

There's another concept that's related to an idea from math in programming: **variables** . (Though we'll see soon an important way in which variables are different in programming).

We can perform a calculation and store the result in a variable, and then when we use that variable's name later, Python will use the value we stored. For example:

.. code-block:: python

        >>> x = 10
        >>> x
        10
        >>> x + 7
        17
        >>> x - 1
        9

In the example above, Python calculated the result 10 in the first line and stored it in a variable named x. In Python, we will call it a **variable declaration** or **variable initialization** the first time we create a variable with =. Then when the program used that name later, Python looked up that stored value and used it in the calculation.

It's worth pointing out that when Python ran the line of code x = 10, there wasn't any answer printed. It wasn't until we used x on a later line that Python printed something out. The variable declaration itself has the effect of creating a variable and doesn't have an answer on its own.

Python lets us declare many variables, and their names aren't restricted to single letters. For example, this short program declares three variables, and uses the first two to calculate the value of the third:

.. code-block:: python

        >>> number_of_professors = 1
        >>> number_of_tas = 2
        >>> number_of_staff = number_of_tas + number_of_professors
        >>> number_of_staff
        3

It's a convention to use _ (pronounced "underscore" or "underbar") to separate words in long variable names in Python. (A fun bit of jargon is that this is called `"snake case" <https://en.wikipedia.org/wiki/Snake_case>`_). It's a good idea to use descriptive names as long as they don't become so long they're prohibitive to type or read.