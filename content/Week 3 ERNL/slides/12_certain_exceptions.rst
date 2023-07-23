Catching only certain exceptions
================================

Let's go back to our input validation example.

.. runner:: 

    try:
        s = input('Please enter a number: ')
        n = int(s) # could fail!
        print('n*n = ' + str(n * n))        
    except:
        print("Uh oh: '" + s + "' isn't a valid number.")
    
What happens if you push ``^C`` (i.e., *control-c*) at the prompt in IDLE? Here's what we get:

.. code-block:: 

    Please enter a number: ^CTraceback (most recent call last):
        File "/home/main.py", line 2, in <module>
            s = input('Please enter a number: ')
    KeyboardInterrupt

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
        File "/home/main.py", line 6, in <module>
            print("Uh oh: '" + s + "' isn't a valid number.")
    NameError: name 's' is not defined

Notice that two exceptions happened. (Yikes! 😬) First, we got a ``KeyboardInterrupt``. That's normal: that's what ``^C`` does. That brought us to the exception handler, where we got another exception, this time because ``s`` isn't defined.

What's going on here? Why wasn't s defined? We were in a ``try``/ ``except``... why did we get a second exception, and why didn't it get handled? Here's what happened in the code: while ``input`` was waiting for user input, pushing ``^C`` caused a ``KeyboardInterrupt``. That exception bubbled up out of ``input`` and into our code, causing us to run the ``except`` block. But that means ``input`` never returned anything to ``s``, so the ``except`` block couldn't even talk about the input... because it never happened!

In general, you don't want to catch *every* exception, just those that you could reasonably respond to. A ``^C`` is a user saying, "Help, get me out of here!", and it's best to let that happen. But the ``ValueError`` from a bad input to ``int`` is eminently handle-able.  In order to catch only certain exceptions, you can name them after the ``except``. Here's a revision of the code:

.. runner:: 

    try:
        s = input('Please enter a number: ')
        n = int(s) # could fail!
        print('n*n = ' + str(n * n))        
    except ValueError:
        print("Uh oh: '" + s + "' isn't a valid number.")

Notice that when using ``^C`` in **IDLE** it works fine, but giving a non-number gives the nice output.

If you care about multiple exceptions, you can write more than one ``except`` clause. Here's an example:

.. runner:: 

    l = list("abcdefghijklmnopqrstuvwxyz")
    try:
        s = input('Which letter of the alphabet do you want to see? ')
        n = int(s) # could fail!
        letter = l[n-1]
        print('Letter ' + str(n) + ' is ' + letter + '.')
    except ValueError:
        print("Uh oh: '" + s + "' isn't a valid number.")
    except IndexError:
        print("Please enter a number between 1 and 26; you entered " + str(n) + ".")

When an exception happens, Python will try each ``except`` in turn, matching the exception thrown against the type named there. It's possible to name more than one:

.. runner:: 

    l = list("abcdefghijklmnopqrstuvwxyz")
    try:
        s = input('Which letter of the alphabet do you want to see? ')
        n = int(s) # could fail!
        letter = l[n-1]
        print('Letter ' + str(n) + ' is ' + letter + '.')
    except (ValueError, IndexError):
        print("Uh oh: '" + s + "' isn't a valid choice.")

The program before this was probably better: it gives more detailed feedback to the user. In any case

The program before this was probably better: it gives more detailed feedback to the user. In any case, Python has `many possible exceptions <https://docs.python.org/3/library/exceptions.html#bltin-exceptions>`_. It's worth getting vaguely acquainted with them!

Finally, Python's ``try``/ ``except`` have more features than we've shown you: ``else`` blocks and ``finally`` blocks. Read the `Python tutorial on Errors and Exceptions <https://docs.python.org/3/tutorial/errors.html>`_ to learn more.