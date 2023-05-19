IDE Testing and Challenge Testing and Quiz Testing:
===================================================

TODO TMR: Work on Pyscript sphinx challenges or find a way to make my own or look at other Pyodide solutions, free response for quizdown

.. py-config::

    splashscreen:
        autoclose: true


First: Standard Repl testing, this is when slides require a user to run a repl but also edit in it!

This example is taken from Week 1 slide 25, using input output
==============================================================    

.. py-repl::
    :output: replOutput

    str1 = input()
    str2 = input()
    combined = str1 + "," + str2
    print(combined)

.. raw:: html

    <div id="replOutput"></div>

.. py-terminal::

