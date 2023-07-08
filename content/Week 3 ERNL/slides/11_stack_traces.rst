Stack traces
============

Let's revisit the breakfast program from the foregoing quiz.

.. runner:: 

    bread = 0

    def make_breakfast():
        fry_eggs()
        toast_bread()

    def fry_eggs():
        print("Sizzle sizzle")
        return

    def buy_bread():
        global bread
        bread = bread + 10

    def toast_bread():
        global bread
        if bread <= 0:
            raise ValueError("out of bread")

        wait_for_toaster()
        return

    def wait_for_toaster():
        print("Ding ding!")
        return

    make_breakfast()

When you run this code, you get a **stack trace**. These traces are invaluable: they tell you what the program stack was when the exception was raised. Here's the program output and trace:

.. code-block:: 

    Sizzle sizzle
    Traceback (most recent call last):
        File "/home/main.py", line 27, in <module>
            make_breakfast()
        File "/home/main.py", line 5, in make_breakfast
            toast_bread()
        File "/home/main.py", line 18, in toast_bread
            raise ValueError("out of bread")
    ValueError: out of bread

Notice a few things. We see the output, ``Sizzle sizzle``, and then the stack trace starts with the word ``Traceback``. Python helpfully informs you that the stack should be read bottom up: the lower the call, the more recent it was to when the exception was thrown. You can read a stack trace like a story:

* At first, we were running at the top-level. (That's ``<module>``.) On line 27, we called ``make_breakfast``.
* When we were running ``make_breakfast``, we called toast_bread on line 5.
* When we were running ``toast_bread``, we raised an exception on line 18. We were out of bread.

There's one more line of output, and it's not really part of the stack trace: it's the default exception handler in Python printing out the exception that made its way to the top level. If an exception is never caught by an ``except`` clause, then Python will print out the exception and exit.