What's On Your Stack?
=====================

Consider the following program (Please run it to see the output):

.. py-config::

    splashscreen:
        autoclose: true

.. py-repl::
    :output: replOutput

    def func_a():
        func_d()
        func_b()
        return

    def func_b():
        return

    def func_c():
        func_b()
        func_e()
        return

    def func_d():
        func_c()
        return

    def func_e():
        print("HERE!")
        return

    func_a()

.. raw:: html

    <div id="replOutput"></div>

.. py-terminal::

Please answer the following two questions about the program. Note that the quiz checker wants *exact* answers! (Func1,Func2,Func3...etc, the last one should have no comma at the end).

.. add-css:: 

.. free-response::
    :question: What order will the functions be called in? Write each function name once per line. If a function is called more than once, list it once for each time its called.
    :correct_answer: func_a, func_d, func_c, func_b, func_e, func_b
    :explanation: The functions will be called in this order: <code> <br> func_a <br> func_d <br> func_c <br> func_b <br> func_e <br> func_b </code>
    :question_num: 1

.. free-response::
    :question: When <code>func_e</code> is called, it will print out <code>HERE!</code>. What is the call stack right before the <code>print</code> happens? Please list it in top down order: the current function, its caller, then its caller, and so on. Put one function name per line.
    :correct_answer: func_e, func_c, func_d, func_a
    :explanation: The functions will be called in this order: <code> <br> func_e <br> func_c <br> func_d <br> func_a
    :question_num: 2