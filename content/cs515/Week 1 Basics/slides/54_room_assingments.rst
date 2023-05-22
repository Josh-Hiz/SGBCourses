Room Assignments
================

Given the following function assign_room(num_students), identify what each function calls will be return.

.. code-block:: python

    def assign_room(num_students):
        if num_students <= 146:
            return "GS 216"
        elif num_students <= 196:
            return "Babbio"
        elif num_students <= 295:
            return "Pier A"
        return "no room"

.. add-css:: 

.. free-response::
    :question: What does <code>assign_room(100)</code> return?
    :correct_answer: "GS 216"
    :explanation: Correct answer is "GS 216"
    :question_num: 1

.. free-response::
    :question: What does <code>assign_room(150)</code> return?
    :correct_answer: "Babbio"
    :explanation: Correct answer is "Babbio"
    :question_num: 2

.. free-response::
    :question: What does <code>assign_room(200)</code> return?
    :correct_answer: "Pier A"
    :explanation: Correct answer is "Pier A"
    :question_num: 3

.. free-response::
    :question: What does <code>assign_room(300)</code> return?
    :correct_answer: "no room"
    :explanation: Correct answer is "no room"
    :question_num: 4