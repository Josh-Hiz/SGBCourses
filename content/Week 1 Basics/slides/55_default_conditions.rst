Default Conditions
==================

else clause
-----------

The last type of clause that can be used in an if statement is an else clause. Else clauses are different from if and elif clauses in that they do not have a boolean condition and act as a catch-all or default for remaining cases when the preceding if and elif clause conditions evaluate to ``False``. Additionally, if an else clause is included in an if statement, it must be the last clause and there is at most one such else clause. Here is a schematic if statement that includes an else clause:

.. code-block::

    if <condition 1>:
        <body 1>
    else:
        <body 2>

Here, if ``<condition 1>`` is ``True``, then ``<body 1>`` is evaluated and the evaluation of the if statement is done. Otherwise, if ``<condition 1>`` is ``False``, then ``<body 1>`` is **not** evaluated and ``<body 2>`` is evaluated, and then the evaluation of the if statement is done.

Here's an example:

.. code-block:: python

    def calculate_num_tas(num_students):
        if num_students <= 100:
            num_tas = 1
        elif num_students <= 200:
            num_tas = 2
        else:
            num_tas = 3
        return num_tas

In this example, if ``num_students`` is less than or equal to 100, then ``num_tas`` is defined to be 1. If ``num_students`` is greater than 100 and less than or equal to 200, then ``num_tas`` is defined to be 2. If ``num_students`` is any other value (in this case it is if ``num_students`` is greater than 200), then ``num_tas`` is defined to be 3.

Something interesting happened here that we didn't do before. We've put a variable initialization in each clause of the if statement. When the if statement runs, exactly one of those variable initializations will be evaluated, setting the value of ``num_tas`` for after the if statement, where the value is returned. This conditional initialization of a variable is a common programming pattern in Python.

In if statements with else clauses, the body of one of the clauses will always be evaluated. If none of the if or elif clause bodies are evaluated, then the else clause body will be evaluated.