Infinite while loops
====================

We have learned that we can use ``while`` loops in order to repeat a block of code until an exit condition is reached. However, what will happen if we set our loop condition simply as ``True``? This will make your code run the body statements indefinitely, since running the body statements does not change the value of the condition, and such a loop is called an infinite loop. The general form is as follows.

.. code-block:: 

    while True:
        <Statements>

``<Statements>`` will be executed repeatedly until the users manually terminates the program or your program crashes. For instance, the following is a ``while`` loop that takes in your name as input and prints it out indefinitely.

.. runner:: 

    while True:
        name = input('Please enter your name: ')
        print('You entered ' + name)
    print('Program ended')

Here's a possible output:

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
    Please enter your name: ^C
    Traceback (most recent call last):
    File "/home/main.py", line 2, in <module>
        name = input('Please enter your name: ')
    KeyboardInterrupt

As the condition is set as ``True`` and it never turns into ``False``, the while loop asks you to enter your name and shows it indefinitely until you hit *control + C* (which creates the ``^C`` characters) to manually exit the program. Note that you cannot see the last line of the code ``print('Program ended')`` executed, because the ``while`` loop never ends.

Finally, note that the runner will eventually terminate every computation after a few seconds. On your own computer, you won't be so lucky! Remember you can always hit *control + C* to "interrupt" a program. Depending on your operating system, the Task Manger or the ``kill`` command can come in handy when programs don't respond to interrupts.