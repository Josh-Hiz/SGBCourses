Try/except statements
=====================

Knowing about errors is half the battle. The other half is handling them. There are two approaches to handling errors, and both are important.

1. **Avoid errors in the first place!** Before doing division, prove to yourself that you won't be dividing by zero; before indexing into a list or string, prove to yourself that the index is in range; before adding two things together, make sure they're both numbers (or both strings, or both lists, etc.).
2. **Handle errors when they happen!** Find places in your code where you can recover from errors, whether that means redoing a computation differently or simply warning the user that things went wrong.

Avoiding errors is a great practice, but it's not always possible: there's no way to avoid a user entering a bad filename; nothing you can do locally, on your computer, will ensure that remote computers are functioning correctly.

Later in this lesson, we'll learn some techniques for avoiding type errors. For now, we'll focus on handling errors.

The main way to handle an error is to explicitly mark code that could fail with a ``try`` and then use ``except`` to catch the exception. Here's an example of an input validation using ``try``/ ``except``:

.. runner:: 

    try:
        s = input('Please enter a number: ')
        n = int(s) # could fail!
        print('n*n = ' + str(n * n))        
    except:
        print("Uh oh: '" + s + "' isn't a valid number.")

How does that code work? The program takes user input ``s`` and tries to convert it to a number ``n``. The call to ``int`` will raise ``ValueError`` if ``s`` isn't a valid base-10 number. If the conversion is successful, the ``break`` will break out of the loop and we'll see the square of the inputted number. If the conversion fails, the ``except`` block runs, printing the error message.

There are a few things to notice:

* The try block runs until an exception occurs.
* The except block only runs when there is an exception.
* Once an exception happens, control never returns to the try block.

We can model ``try``/ ``except`` as follows. Suppose we're given:

.. code-block:: 

    try:
        <STMT1>
        ...
        <STMTn>
    except:
        <HANDLER>

1. Run STMT1. If an exception occurs, run HANDLER. Otherwise...
2. Run STMT2. If an exception occurs, run HANDLER. Otherwise...
3. ...
4. Run STMTn. If an exception occurs, run HANDLER. Otherwise, you're done.