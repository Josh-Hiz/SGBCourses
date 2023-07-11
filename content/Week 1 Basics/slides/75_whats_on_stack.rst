What's On Your Stack?
=====================

Consider the following program (Please run it to see the output):

.. runner::

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


Please answer the following two questions about the program. Note that the quiz checker wants *exact* answers! (Func1,Func2,Func3...etc, the last one should have no comma at the end).

.. free-r:: 
    :answer:
        func_a
        func_d
        func_c
        func_b
        func_e
        func_b
    
    # Question 1

    What order will the functions be called in? Write each function name once per line. If a function is called more than once, list it once for each time its called.
    
    >>>
    The functions will be called in this order:<br>
    ```
    func_a
    func_d
    func_c
    func_b
    func_e
    func_b
    ```

.. free-r:: 
    :answer:
        func_e
        func_c
        func_d
        func_a
    
    # Question 2

    When ```func_e``` is called, it will print out ```HERE!```. What is the call stack right before the print happens? Please list it in top down order: the current function, its caller, then its caller, and so on. Put one function name per line.

    >>>
    The stack will be, from the current caller on down:

    ```
    func_e
    func_c
    func_d
    func_a
    ```