Adding/deleting practice
========================

Suppose we start with the following dictionary:

.. code-block:: 

    problem_dict = {'CS' : '515A', 'MUS' : '2A', 'MATH' : '10A'}

Then, suppose we run the following two lines of code.

.. code-block:: 

    problem_dict['PHYS'] = '2A'

and

.. code-block:: 

    del problem_dict['MUS']

.. add-css::

.. free-response::
    :question: What will be printed when we run <code>print(problem_dict)</code>?
    :correct_answer: {'CS': '515A', 'MATH': '10A', 'PHYS': '2A'}
    :explanation: Correct answer is {'CS': '515A', 'MATH': '10A', 'PHYS': '2A'}
    :question_num: 1