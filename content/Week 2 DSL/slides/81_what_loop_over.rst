What should we loop over?
=========================

Recall the ``recipients`` dictionary:

.. code-block::

    recipients = {'Physics': 409, 'Biology': 1473, 'Mechanical Engineering': 1343, 
    'Physical Sciences': 1131, 'Electrical Engineering': 153, 'Business': 131, 'Computer Science': 2870}

What do you need to replace ``FILL_ME`` in the following code to have the output below?

.. code-block:: 

    for i in FILL_ME:
        print(i)

Output:

.. code-block:: 

    409
    1473
    1343
    1131
    153
    131
    2870

.. add-css::

.. free-response::
    :question: What do you need to replace <code>FILL_ME</code> in the following code to have the output below?
    :correct_answer: recipients.values()
    :explanation: Correct answer is recipients.values()
    :question_num: 1