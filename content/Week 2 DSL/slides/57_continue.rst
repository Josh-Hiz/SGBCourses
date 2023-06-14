Continue statements
===================

We have learned that ``break`` statements let users to have a control to stop loops under a certain condition even when the loop exit condition remains ``True``. However, what if we want to ``continue`` repeating the loop after skipping some statements? The ``continue`` statement in Python returns to the beginning of the loop to continue with the next iteration. The continue statement skips all the following statements in the current iteration of the loop and starts evaluating the loop condition for the next iteration of the loop. 

 The general form of using a ``continue`` statement in a ``while`` loop is as follows.

.. code-block:: 

    while <Exit Condition>:
        <Statement(s) #1>
        if <Continue Condition>:
            continue
        <Statement(s) #2>

``<Continue Condition>`` can be any boolean expression that represents either ``True`` or ``False``. The block of ``<Statement(s) #1>`` and ``<Statement(s) #2>`` will be implemented repeatedly until ``<Continue Condition>`` becomes satisfied at some point. Once ``<Continue Condition>`` is met, the program skips ``<Statements #2>`` and go on to the next iteration of the loop. To be specific, the progression of a while loop with a break statement is as follows:

Step 1. Check whether ``<Exit Condition>`` is ``True``. If it is ``True``, It continues to Step 2. Otherwise, skip to Step 6.
Step 2. Execute ``<Statements #1>``.
Step 3. Check if ``<Continue Condition>`` is ``True``. If so, skip to Step 1. Otherwise, continue to Step 4.
Step 4. Execute ``<Statements #2>``.
Step 5. Go to Step 1. 
Step 6. Exit the loop.

``continue`` statements can be used in for loops as well. Whether the current iteration for the ``for`` loop is ongoing or not, the ``continue`` statement can skip the following statements when ``<Continue Condition>`` is ``True``. The general form of using a ``continue`` statement in a ``for`` loop is as follows.

.. code-block:: 

    for <member variable> in <sequence>:
        <Statements #1>
        if <Continue Condition>:
            continue
        <Statements #2>

For example, we can use a ``for`` loop and a ``continue`` statement to run a program that prints only the days of a week that an employee works. The employee works only on weekdays.

.. runner:: 

    for day in ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']:
        if day in ['Sun', 'Sat']:
            continue
        print('I work on ' + day)

The ``for`` loop iterates over every day in the list of the days of the week and prints out the day. However, the loop skips the printing part when it is either Sunday or Saturday using the ``continue`` statement. Note that the print statement is executed only for weekdays as shown below.

.. code-block:: 

    I work on Mon
    I work on Tue
    I work on Wed
    I work on Thu
    I work on Fri

The difference between ``break`` and ``continue`` is that the ``break`` statement terminates the loop while the loop will not be terminated due to the ``continue`` statement. Both interrupt the current iteration; ``break`` goes to the end, while ``continue`` goes to the top for the next iteration.