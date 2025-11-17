Name/variable binding errors
============================

When you try to read from a variable that Python hasn't heard of, you get a ``NameError``. Here's an example, where ``x`` isn't bound:

.. runner:: 

    print('hello')

    def missing_x(n):
        return n + x

    print('the result is', missing_x(10))
    print('goodbye')

Observe a few things. The name error doesn't stop our program from running---we see the ``hello`` output. But the ``NameError`` in ``missing_x`` means we don't see output from either of the later ``print`` calls.

It's possible for a program to have *hidden* or *latent* ``NameErrors``. Here's a slight modification of our example:

.. runner:: 

    print('hello')

    def missing_x(n):
        return n + x

    def other_fun(n):
        return n + 15

    print('the result is', other_fun(10))
    print('goodbye')

Our program ran correctly to completion. That's good! But if someone ever calls ``missing_x``, they're in a for a nasty ``NameError`` surprise. That's bad! In some programming languages---Java, for example--- ``NameError``'s will prevent you from running your program at all. Python is more relaxed, which means you get to run your program earlier... but also means that your program could have bugs hidden in it.

Like syntax errors, ``NameError``'s aren't really "handled" in the program. The way to avoid ``NameError``'s is to make sure your variable names are correct in your program, just like the way to avoid syntax errors is to make sure your program is syntactically valid.