Catching errors early with assert
=================================

Already in the course, we've asked you to make many assumptions in your code: that input will be properly formed, that functions will only be called with certain values, and so on. Every piece of code makes assumptions about the world. Violating these assumptions leads to various error conditions---sometimes an exception, sometimes just bad behavior. We've seen a lot of exceptions, but not so much in the way of bad behavior. Let's look at the letter example again:

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

What happens when you enter ``0``, and why? You'll notice it picks the letter ``z``, because ``0-1`` is ``-1``, and in Python, indexing with ``-1`` goes from the end of the list. A user would be confused by that output! It would be better if our program gave some kind of error message.

One approach would be to add an ``if``, checking that ``n`` is between 1 and 26, inclusive. Another option is to simply state our assumption in code. A nice way to do that is with ``assert``. Assertions are self checks in your code, saying, "Hey, this had better be true or something is really wrong! Here's an example:

.. runner:: 

    l = list("abcdefghijklmnopqrstuvwxyz")
    try:
        s = input('Which letter of the alphabet do you want to see? ')
        n = int(s) # could fail!
        letter = l[n-1]
        assert 1 <= n <= 26 # ASSERTION
        print('Letter ' + str(n) + ' is ' + letter + '.')
    except ValueError:
        print("Uh oh: '" + s + "' isn't a valid number.")
    except IndexError:
        print("Please enter a number between 1 and 26; you entered " + str(n) + ".")

The new assertion on line 6 is the same as having written:

.. code-block::

    if not (1 <= n <= 26):
        raise AssertionError()

Using ``assert`` is more concise and looks better. In general, ``assert``'s' are a wonderful way to catch bugs, especially 'logic' bugs where your program behaves strangely but doesn't crash.

Better errors with assert
-------------------------

By default, a failed ``assert`` just yields an ``AssertionError``. You can easily write better error messages as follows:

.. runner:: 

    l = list("abcdefghijklmnopqrstuvwxyz")
    try:
        s = input('Which letter of the alphabet do you want to see? ')
        n = int(s) # could fail!
        letter = l[n-1]
        assert 1 <= n <= 26, "input must be between 1 and 26, inclusive"
        print('Letter ' + str(n) + ' is ' + letter + '.')
    except ValueError:
        print("Uh oh: '" + s + "' isn't a valid number.")
    except IndexError:
        print("Please enter a number between 1 and 26; you entered " + str(n) + ".")

Notice that we've used the form ``assert EXPR, MESSAGE``, where ``EXPR`` should evaluate to ``True``; if it doesn't, then we'll raise an ``AssertionError`` with ``MESSAGE`` contained in it.