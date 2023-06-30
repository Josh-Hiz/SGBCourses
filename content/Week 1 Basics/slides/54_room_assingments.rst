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

.. free-r::
    :answer: "GS 216"

    # Question 1

    What will ```assign_room(100)``` return?

.. free-r::
    :answer: "Babbio"

    # Question 2

    What will ```assign_room(150)``` return?

.. free-r::
    :answer: "Pier A"

    # Question 3

    What will ```assign_room(200)``` return?


.. free-r::
    :answer: "no room"

    # Question 4

    What will ```assign_room(300)``` return?