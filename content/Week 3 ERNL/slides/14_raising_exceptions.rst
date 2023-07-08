Raising exceptions
==================

We've seen how to handle exceptions, and we've all definitely written code that raises exceptions. Sometimes your code is in a bad state and there's nothing you can do locally to solve the problem. In such a case, the right choice is to raise an exception. Here's an example related to input validation: a poorly chosen user password

.. runner:: 

    # load a list of words
    words = open('/usr/share/dict/words').read().split('\n')

    # have the user pick a password
    passwd = input('Enter a password: ')
    if passwd in words:
        raise ValueError("That's not a very good password!")
    print("'" + passwd + "' isn't in the dictionary... looks good!")

The ``raise`` keyword will raise an exception. Typically it'll be of the form ``raise BlahError("description of what went wrong")``; in the example above, we use ``ValueError`` in exactly that way. You can only raise exceptions; `Python has many built-in exceptions <https://docs.python.org/3/library/exceptions.html#bltin-exceptions>`_, and you should generally use those. For example, raising a ``ValueError`` when given a bad value, or ``IndexError`` when something is out of bounds. We'll learn later in the semester how to create our own exceptions. If you can't find anything builtin that's a good match, you can always raise a ``RuntimeError``.