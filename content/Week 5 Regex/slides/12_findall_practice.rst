re.findall practice
===================

.. free-r:: 
    :answer: ['x', 'y', 'l', 'p', 'h', 'n']

    # Question 1

    What is the result of ```re.findall("[^aeiou]","xylophone")```?

.. free-r:: 
    :answer: ['pet', 'pot', 'p t']

    # Question 2

    What is the result of ```re.findall("p.t", "My pet pot is in tip top shape.")```?

.. quizdown:: 

    # Which of the following definitions of ```s``` will make ```re.findall("par..t", s)``` return a non-empty list?

    - [x] ```s = parrot```
    - [ ] ```s = partial```
    - [ ] ```s = part```
    - [x] ```s = parent```