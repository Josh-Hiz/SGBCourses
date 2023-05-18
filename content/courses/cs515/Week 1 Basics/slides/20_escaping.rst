Escaping
========

.. py-config::

    splashscreen:
        autoclose: true


When writing strings, the backslash character ``\`` is used to "escape" special characters. That is, backslash is a signal to interpret the *next* character differently. We've seen this with quotes already. Another good example is ``\n``, which represents a newline. There are plenty of others, like ``\t`` to mean a "tab" (nominally, 4 or 8 spaces, but displayed in an "aligned" way).

.. py-repl::
    :output: replOutput

    print('This\tTabs\nis\tare\non\tweird!\nfive\tDo you\nlines.\tsee?')


We also used the backslash character to work with quotes:

.. py-repl::
    :output: replOutput

    print('I hope I didn\'t mess this up!')
    print("\"Oh no,\" she said, \"I'm sure you got it right.\"")


And if you want to write a literal backslash, you just write two of them, to "escape" the second backslash and turn off its special meaning:

.. py-repl::
    :output: replOutput

    print("Here's a backslash: \\")

.. raw:: html

    <div id="replOutput"></div>

.. py-terminal::