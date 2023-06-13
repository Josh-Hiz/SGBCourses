Tracing a while loop
====================

Consider the following snippet of code.

.. code-block:: 

    upper_bound = 10
    num = 2
    while num < upper_bound:    # line A
        num *= 2                # line B

.. add-css:: 

.. free-response::
    :question: Trace through the loop step by step to see how the value of ``num`` changes. What is the value of ``num`` after we exit the loop?
    :correct_answer: 16
    :explanation: Correct answer is 16
    :question_num: 1

.. quizdown:: 

    ## How many times is line A executed and how many times is line B executed?

    Try to trace through this on your own, but if you get stuck, try [using Python Tutor](https://pythontutor.com/visualize.html#mode=display).

    1. [ ] A: 3, B: 3
    2. [ ] A: 3, B: 4
    3. [x] A: 4, B: 3
    4. [ ] A: 4, B: 4