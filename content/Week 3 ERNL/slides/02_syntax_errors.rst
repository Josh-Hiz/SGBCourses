Syntax errors
=============

Syntax errors are special: if your program has a syntax error, you never even get to run it. Here's an example where we're missing a colon after a function definition:

.. runner:: 

    print('hello')

    def do_nothing(x)
        return x

    print(do_nothing('goodbye'))

Notice that the program never runs *at all*---we never see the ``hello`` message even though the call to ``print`` comes before bad definition of ``do_nothing``.

Syntax errors can't really be "handled" in a program: you just have to fix your program's syntax!