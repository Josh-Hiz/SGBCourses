Special characters, escape characters, and raw strings
======================================================

So far we've seen how to write regular expressions, using the ``.`` and ``[]`` and ``^`` and ``-`` and ``\`` characters for some special purposes. You might have two questions:

1. What if you want to match one of those characters?
2. Doesn't ``\`` do special things in Python?

These are tricky points! Some languages have a special syntax for regular expressions, which can simplify some of the issues here. Python's situation is a little bit more complicated. Let's take it from the top.

Escaping
--------

When writing strings, the backslash character ``\`` is used to "escape" special characters. That is, backslash is a signal to interpret the *next* character differently. We've already seen this with ``\n``, which represents a newline. There are plenty of others, like ``\t`` to mean a "tab" (nominally, 4 or 8 spaces, but displayed in an "aligned" way).

.. runner:: 

    print('This\tTabs\nis\tare\non\tweird!\nfive\tDo you\nlines.\tsee?')

We've also used the backslash character to work with quotes:

.. runner:: 

    print('I hope I didn\'t mess this up!')
    print("\"Oh no,\" she said, \"I'm sure you got it right.\"")

And if you want to write a literal backslash, you just write two of them, to "escape" the second backslash and turn off its special meaning:

.. runner:: 

    print("Here's a backslash: \\")


Escaping in regular expressions
-------------------------------

To write a regular expression that matches against a literal dot, you just need to escape it, i.e., ``\w\w\w\.py`` matches ``abc.py`` and the end of ``food.py``, but not ``snoopy``.

Backslashes in Python regular expressions
-----------------------------------------

In Python, regular expressions start out as strings. Strings are a very handy interface---regular expressions are quite like the strings that they match against---but there's a problem. Strings already use backslash for their own escaping!

To see the problem, suppose we wanted to write a regular expression matching the literal string ``\newpage``. If we just write ``'\newpage'`` in Python, we might not like the result:

.. runner:: 

    print('here we go...')
    print('\newpage')

Oops! The ``\n`` got interpreted as a newline. To solve the problem, we can escape the first backslash, like so:

.. runner:: 

    print('here we go...')
    print('\\newpage')

Great! But it turns out that Python's regular expression parser will see that single backslash followed by an ``n`` and get confused:

.. runner:: 

    import re

    print(re.findall('\\newpage', '\\newpage'))

The solution is to make sure the regex sees *two* backslashes, so that those are escaped internally. That is, we need to write:

.. runner:: 

    import re

    print(re.findall('\\\\newpage', '\\newpage'))

Ouch! That's a lot of slashes. There's a better way.

Raw strings
-----------

Python supports a special syntax for `raw strings <https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals>`_, written ``r"..."``. The 'r' stand for "raw" and it indicates that backslashes should not be an escape character, but should be interpreted exactly as is (`more or less <https://docs.python.org/3/faq/design.html#why-can-t-raw-strings-r-strings-end-with-a-backslash>`_).

So we could instead write:

.. runner:: 

    import re

    print(re.findall(r'\\newpage', '\\newpage'))

It's not always necessary to use raw strings---if you write a backslash before characters that Python doesn't normally do anything for, it leaves the backslash and the character in:

.. runner:: 

    print('\.')

Which means that you don't have to worry about raw strings or multiple backslashes for escaping most things, only for any of the `following characters treated specially <https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals>`_: ``\'"abfnNrtuUvx`` and digits. But keeping track of that list is tricky---why not avoid a nasty, hard-to-understand bug and use raw strings?

A common mistake
----------------

Especially when thinking about numbers, it is a common mistake to write a literal ``.`` instead of the escaped one.

.. runner:: 

    import re

    print(re.findall("3.14", "3.1415"))
    print(re.findall("3.14", "301415"))

Character class nuances
-----------------------

Finally, character classes have their own nuances.

* If you want to include ``]`` in a character class, either escape it with a backslash or put it first.
* If you want to include ``-`` in a character class, either escape it with a backslash or put it first or last.
* If you want to include ``^`` in a character class, don't make it the first character.