Errors that end your program early
==================================

It's inevitable: things go wrong in your program, causing it to terminate early. There are a number of ways this can happen:

1. Syntax errors mean you can't even run your program, like ``def do_nothing(x) return x``.
2. Reading from an undefined variable might crash your program when it runs, like ``def f(x): return x + n``.
3. Misusing values might lead to a type error, like ``1 + 'hi'``.
4. Some operations are *partial*, like division or ``list.index``.
5. Someone could hit ``^C`` (i.e., *control-c*) and interrupt your program.
6. Someone could turn off the computer, e.g., the battery dies.

Each of these circumstances is some kind of error. Programmers spend a great deal of time anticipating, avoiding, and handling errors. Let's look at each kind of error in turn.

A bit of nomenclature: in general computing, error and exception are more or less synonymous. But in Python, an error is a particular kind of exception. For now, we can treat the terms as synonymous.