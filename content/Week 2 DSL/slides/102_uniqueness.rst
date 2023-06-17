Uniqueness
==========

Suppose we run the following code:

.. code-block:: python

    s = set()
    s.add(False)
    s.add(0)
    print(s)

.. add-css::

.. free-response::
    :question: What is the output?
    :correct_answer: {False}
    :explanation: Correct answer is {False}
    :question_num: 1

Suppose we run the following code:

.. code-block:: 

    s = set()
    s.add(False)
    s.add(1)
    s.add(0)
    s.add(True)
    print(s)

.. free-response::
    :question: What is the output?
    :correct_answer: {False, 1}
    :explanation: Correct answer is {False, 1}
    :question_num: 2
