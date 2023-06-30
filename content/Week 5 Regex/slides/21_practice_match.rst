Practice with Match objects
===========================

.. code-block:: 

    import re

    email = r"((?:\w+\s*)*) <([^@]+@[^@]+)>"
    m = re.fullmatch(email, "Michael Greenberg <michael.greenberg@stevens.edu>")

.. free-r:: 
    :answer: Michael Greenberg

    # Question 1

    What is ```m.group(1)```? No need to write quotes.

.. free-r:: 
    :answer: michael.greenberg@stevens.edu

    # Question 2

    What is ```m.group(2)```? No need to write quotes.