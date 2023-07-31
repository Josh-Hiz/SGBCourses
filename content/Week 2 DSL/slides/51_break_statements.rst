Break statements
================

If this endless loop will run until it may lead to the program crashing, why would we use it? Such loops are meaningful especially for cases where the program demands to repeat unconditionally until users provide some signal to stop the loop. ``break`` statement is used in loops to indicate such stop signals, i.e., in what conditions the loop can be ended regardless of whether the loop exit condition is satisfied.

The form of a ``while`` loop with a ``break`` statement is as follows.

.. code-block::

    while True:
        <Statement(s) #1>
        if <Break Condition>:
            break
        <Statement(s) #2>

``<Break Condition>`` can be any boolean expression that represents either ``True`` or ``False``. The block of ``<Statement(s) #1>`` and ``<Statement(s) #2>`` will be implemented repeatedly until ``<Break Condition>`` becomes satisfied at some point. Once ``<Break Condition>`` is met, the while loop is stopped without executing ``<Statement(s) #2>``. To be specific, the progression of a while loop with a break statement is as follows:

Step 1. Check whether the exit condition of the ``while`` loop is ``True``, which is always the case for infinite loops. Continue to Step 2.

Step 2. Execute ``<Statement(s) #1>``.

Step 3. Check if ``<Break Condition>`` is True. If so, end the ``while`` loop and skip to Step 6. Otherwise, continue to Step 4.

Step 4. Execute ``<Statements #2>``.

Step 5. Go to Step 1. 

Step 6. Exit the loop. 

Now, we are ready to see an example that uses an infinite ``while`` loop with a ``break`` statement. Let's go back to the infinite name-prompt program, with an additional feature that the user can type 'stop' to exit the loop. We set this feature with lowercase 'stop' so that even if the name of a user happens to be 'Stop', the program can tell whether the input is a stop signal or the name of the user.

.. runner:: 

    while True:
        name = input('Please enter your name: ')
        if name == 'stop':
            break
        print('You entered ' + name)
    print('Program ended')

Here is the result.

.. code-block::

    Please enter your name: Gerald
    You entered Gerald
    Please enter your name: Sorin
    You entered Sorin
    Please enter your name: Yeohee
    You entered Yeohee
    Please enter your name: Annie
    You entered Annie
    Please enter your name: Winny
    You entered Winny
    Please enter your name: stop
    Program ended

As expected, the loop keeps taking input and printing the name until you type 'stop', which turns the condition of the ``break`` statement from ``False`` into ``True``.