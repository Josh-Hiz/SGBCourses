While loops
===========

With ``for`` loops added to our programming tool set, we now have a way to run blocks of code repeatedly. ``for`` loops give us the ability to run blocks of code a **definite** number of times - we know exactly how many iterations a ``for`` loop will run. But what if we don't know ahead of time how many times we'd like to repeat a block of code? ``while`` loops give us the ability to repeat executing blocks of code **indefinitely** until an exit condition is reached. Here is the general form that a ``while`` loop takes in python:

.. code-block:: 

    while some_condition:
        # statements to execute go here in the loop body

Here, ``some_condition`` can refer to any boolean expression (an expression that evaluates to ``True`` or ``False``). A ``while`` loop will first check that ``some_condition`` is ``True`` and if so, then execute the loop body. Once the loop body completes, ``some_condition`` is checked again, and if it's ``True``, it will enter the body again. This process repeats until the evaluation of ``some_condition`` is ``False``. Here is a more concrete representation of the progression of executing a ``while`` loop:

*Step 1*. Check if the condition is ``True``. If yes, continue to Step 2. If not, skip to Step 4.
*Step 2*. Execute the statements in the loop body.
*Step 3*. Repeat Step 1.
*Step 4*. Exit the loop. Don’t execute the loop body, and instead proceed with executing the code after the loop.

The most important thing to note is that the condition is only checked once at the beginning of each potential iteration. This means that if the condition is ``True`` and we entered the loop body, the condition isn't checked again until after the whole loop body is executed. You can think of a ``while`` loop like a repeating ``if`` statement.

Here is an example of a ``while`` loop that repeatedly subtracts 6 from some number ``num`` until ``num`` becomes negative:

.. runner:: 

    num = 25
    while num >= 0:   # if num is non-negative, enter the loop body
        num = num - 6      # subtract 6 from num
        print('num is ' + str(num))

After the loop exits, the value of ``num`` is **-5**. Go to the Python Tutor link below and copy and paste these lines there. Then run it to see a more detailed view of the order in which the lines are executed and how the variable ``num`` is updated in each iteration.

A great tool to use here is Python Tutor, which can visualize each step of simple Python programs. `Try it out! <https://pythontutor.com/visualize.html#mode=display>`_

If it were possible, note that the above ``while`` loop would be equivalent to having an indefinite number of nested ``if`` statements checking the same condition and subtracting 6 if ``True``:

.. code-block:: 

    num = 25
    if num >= 0:
        num = num - 6
        if num >= 0:
            num = num - 6
            if num >= 0:
                num = num - 6
                .
                .
                .