Interruptions from the user and the environment
===============================================

The first four sources of errors---syntax errors, name/binding errors, type errors, and partial operations---are all intrinsic to your program. While type errors and partial operation errors might only be triggered by certain inputs, the program itself is in some sense responsible for these failures. The last two things we listed that could disrupt your program are extrinsic sources of error. The user could interrupt your program by typing ``^C`` (i.e., *control-c*) or using the Task Manager or ``kill`` to stop the Python process; the computer's battery could die or water could spill over your computer and short the connections.

It's tricky to demonstrate a user interrupt, and it's a downright bad idea to spill water on your computer just to see what would happen! But here's an infinite loop; click 'Run' and push ``^C`` after a second.

.. runner:: 

    while True:
        pass

You should get output like:

.. code-block:: 

    ^CTraceback (most recent call last):
    File "/home/main.py", line 2, in <module>
        pass
    KeyboardInterrupt

Here, ``KeyboardInterrupt`` is how Python models the ``^C`` interrupt. There should also be a message in red saying "Program exited with signal 2 (SIGINT - Interrupt)" from Ed. By default, typing ``^C`` will send SIGINT---the interrupt signal---the current process.

Another possibility is an early end of input. Consider the following program:

.. runner:: 

    name = input("What's your name? ")
    print('Hi, ' + name + '!')

If you type ``^D`` (i.e., *control-d*) at the prompt, you'll get something like:

.. code-block:: 

    What's your name? Traceback (most recent call last):
    File "/home/main.py", line 1, in <module>
        name = input("What's your name? ")
    EOFError

Along with a red banner from Ed saying "Program exited with code 1". The ``EOF`` in ``EOFError`` stands for "end of file"---the Python program wanted to read some input but ``^D`` in a command-line environment means "there's no more input here". Since the program needs input to continue, we get the ``EOFError``.

In the case of a catastrophe where the computer just stops working, there's really nothing to be done. Your program may not even get a message, but things may simply suddenly stop. It happens! 🤷‍♀️