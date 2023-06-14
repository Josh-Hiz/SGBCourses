Break statements in for loops
=============================

``break`` statements can be used in ``for`` loops similarly as they were used in while loops. Whether the sequence in the ``for`` loop is fully iterated or not, the ``break`` statement can exit the ``for`` loop once the break condition becomes ``True``. 

The general form of using a ``break`` statement in a ``for`` loop is as follows.

.. code-block:: 

    for <variable> in <sequence>:
        <Statement(s) #1>
        if <Break Condition>:
            break
        <Statement(s) #2>

``<Statement(s) #1>`` and ``<Statement(s) #2>`` are repeated as a member variable iterates within sequence, until ``<Break Condition>`` becomes true, in which case the loop is finished without further implementing ``<Statements #2>``. 

Let's go back to our summation example, with an additional feature that the user can stop in the middle of the summing process once a specific number is reached. Assume that we have a calculator that sums from 1 to 10 but the user wants to just sum up till 3. 

.. runner:: 

    total_sum = 0
    for num in range(10):
        print('The current number: ', num)
        total_sum += num
        if num == 3:
            break
    print('The sum is: ', total_sum)

Then, here is the output.

.. code-block:: 

    The current number:  0
    The current number:  1
    The current number:  2
    The current number:  3
    The sum is:  6

Note that although ``for`` loop is designed so it is iterated 10 times, it was actually put to stop at the 4th repetition (or iteration).