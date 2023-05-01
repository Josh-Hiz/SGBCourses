More Conditions
===============

**elif clause**

Additionally, we can evaluate code based on more than one condition in an if statement by including *elif clauses*. (The keyword ``elif`` can be read as "else if".)

.. code-block::

    if <condition 1>:
        <body 1>
    elif <condition 2>:
        <body 2>

Whenever using "elif", we always need an if clause first, followed by as many elif clauses as we would like. The code snipped above is evaluated in the order as follows:

* if ``<condition 1>`` is ``True``, then ``<body 1>`` is evaluated, and the entire if statement is done being evaluated
* otherwise, if ``<condition 1>`` is ``False``, then ``<body 1>`` is **not** evaluated and the if statement continues to be evaluated in the next clause
* in the elif clause, if ``<condition 2>`` is ``True``, then ``<body 2>`` is evaluated and the entire if statement is done being evaluated
* otherwise, if ``<condition 2>`` is False, then ``<body 2>`` is not evaluated and the if statement continues to be evaluated in the next clause. Since there is no "next clause", the entire if statement is done being evaluated

One thing to note is that in a sequence of if-elif clauses, at most **one** of the bodies of the clauses will be evaluated, if any.

Here's an example:

.. code-block:: python

    if num_students <= 100:
        num_tas = 1
    elif num_students <= 200:
        num_tas = 2
    elif num_students <= 300:
        num_tas = 3

In this example, depending on the value of ``num_students``, ``num_tas`` is assigned a different value.

Let's trace through this code in the case where ``num_students`` is 150:

* First, ``num_students <= 100`` is evaluated. This evaluates to ``False``, so the body of the if clause is not evaluated and the if statement continues to be evaluated in the next clause
* Next, ``num_students <= 200`` is evaluated. This evaluates to ``True``, so the body of this elif clause is evaluated and the if statement as a whole is done being evaluated since the body of one of the clauses has been evaluated.

Now let's trace through this code in the case where ``num_students = 400``:

* First, ``num_students <= 100`` is evaluated. This evaluates to ``False``, so the body of the if clause is not evaluated and the if statement continues to be evaluated in the next clause
* Next, ``num_students <= 200`` is evaluated. This evaluates to ``False``, so the body of this elif clause is not evaluated and the if statement continues to be evaluated in the next clause
* Next, ``num_students <= 300`` is evaluated. This evaluates to ``False``, so the body of this elif clause is not evaluated and the if statement continues to be evaluated in the next clause. Since there are no more clauses in the if statement, the if statement is done being evaluated.
  
There are two ways an if-elif statements can finish being evaluated:

* The body of one of its clauses is evaluated
* None of the clause bodies are evaluated and the end of the if statement is reached (no more clauses)