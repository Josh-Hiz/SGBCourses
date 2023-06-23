re.findall practice
===================

.. add-css::

.. free-response::
    :question: What is the result of <code>re.findall("[^aeiou]","xylophone")</code>?
    :correct_answer: ['x', 'y', 'l', 'p', 'h', 'n']
    :explanation: The correct answer is ['x', 'y', 'l', 'p', 'h', 'n']
    :question_num: 1

.. free-response::
    :question: What is the result of <code>re.findall("p.t", "My pet pot is in tip top shape.")</code>?
    :correct_answer: ['pet', 'pot', 'p t']
    :explanation: The correct answer is ['pet', 'pot', 'p t']
    :question_num: 2

.. quizdown:: 

    # Which of the following definitions of ```s``` will make ```re.findall("par..t", s)``` return a non-empty list?

    - [x] ```s = parrot```
    - [ ] ```s = partial```
    - [ ] ```s = part```
    - [x] ```s = parent```