Practice with Match objects
===========================

.. code-block:: 

    import re

    email = r"((?:\w+\s*)*) <([^@]+@[^@]+)>"
    m = re.fullmatch(email, "Michael Greenberg <michael.greenberg@stevens.edu>")

.. add-css:: 

.. free-response::
    :question: What is <code>m.group(1)</code>? No need to write quotes.
    :correct_answer: Michael Greenberg
    :explanation: The correct answer is Michael Greenberg
    :question_num: 1

.. free-response::
    :question: What is <code>m.group(2)</code>? No need to write quotes.
    :correct_answer: michael.greenberg@stevens.edu
    :explanation: The correct answer is michael.greenberg@stevens.edu
    :question_num: 2