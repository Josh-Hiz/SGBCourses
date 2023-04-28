Defining Our Own Functions
==========================

Sometimes we'll have a calculation we want to do over and over again. For example, the sum of squares of numbers is a common and important metric in statistics, geometry, and elsewhere. (For example, Euclidean distance is the square root of the sum of squares.) We could repeatedly write out the arithmetic each time we needed it:

.. code-block::

    num1 = ...
    num2 = ...
    num3 = ...
    num4 = ...
    answer1 = num1 * num1 + num2 * num2
    answer2 = num3 * num3 + num4 * num4
    ...

Writing it out like this is fine for short calculations, but longer ones (like, say, calculating the Euclidean distance between two points, or a more complicated statistical measure), are tedious and error-prone to type out repeatedly. Even copy-pasting isn't that great, because it's easy to make errors when renaming the variables. If you find a bug in one version, you have to find all of the copy-pasted versions and fix those, too! Copy-pasting code is generally not a great idea.

This motivates a crucial and fundamental programming idea, which is writing our own **function definitions**.

We can write our own function that returns the sum of squares of two numbers:

.. code-block:: python

    def sum_of_squares(n1, n2):
        return n1 * n1 + n2 * n2

Here, we say that

* ``sum_of_squares`` is the **funciton name**
* ``n1`` and ``n2`` are the **parameters** or **argument names** or the **formal arguments** of the function 
* ``return n1 * n1 + n2 * n2`` is the **body** of the function

In addition, **return** and **def** are examples of **keywords**. They are part of the Python language and have special meaning as part of function definitions. **def** tells Python that this line (and potentially the next few lines) will describe a function. **return** tells Python to evaluate the expression after it and make that be the result of the current function call – we'll describe that in a minute.

It's also required that all the lines that are part of the **function body** be indented (in this case by 2 spaces). If there's more than one line, they must be indented the same amount (with some important exceptions we'll see in later chapters).

If we run this module and interact with it, we can call the ``sum_of_squares`` function just like we could call ``max`` or ``abs``:

.. code-block:: python

    >>> sum_of_squares(4, 5)
    41
    >>> sum_of_squares(1, 2)
    5

We can describe how a call to ``sum_of_squares`` works as follows.

To evaluate ``sum_of_squares(4, 5)``, Python:

* evaluates the **body** of the ``sum_of_squares`` function,
* **substituting** the values of the **actual arguments** (4 and 5) for the **formal arguments** (``n1`` and ``n2``)
* when the expression after the ``return`` has the final value, that value is the value of the whole function call

So we could think of evaluation taking these steps:

.. code-block::

    sum_of_squares(4, 5)
    -> return 4 * 4 + 5 * 5 
    -> return 16 + 25 
    -> return 41 
    -> 41

The first step is where the argument values are substituted for ``n1`` and ``n2``. Then we do some arithmetic as usual, and then the final value, 41, is the result of the function call.

We can define functions that work with strings (and any other datatype we see in the future), too. For example, we could write a function that fills in a sentence:

.. code-block:: python

    def fill_in(adjective, noun):
        return "The " + adjective + " " + noun + " wasn't very inspired."

Let's run it:

.. code-block:: python

    >>> fill_in("first", "example")
    "The first example wasn't very inspired."
    >>> fill_in("third", "sequel")
    "The third sequel wasn't very inspired."

In both of these cases, we can see the same rules as before: The function call takes the argument values (like ``"third"`` and ``"sequel"``), and uses them for the values of the parameters (the variables ``adjective`` and ``noun``). Then the result of the whole function call expression is the result of the expression after ``return``.

