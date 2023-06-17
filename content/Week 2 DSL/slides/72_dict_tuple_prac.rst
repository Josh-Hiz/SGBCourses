Dictionary and tuple practice
=============================

.. code-block:: 

    cities = {(32.7157, 117.1611): 'San Diego', (37.7749, 122.4194): 'San Francisco',
              (40.7128, 74.006): 'New York', (30.2672, 97.7431): 'Austin'}

    coordinates = {'San Diego': (32.7157, 117.1611), 'San Francisco': (37.7749, 122.4194),
                   'New York': (40.7128, 74.006), 'Austin': (30.2672, 97.7431)}

.. add-css::


.. free-response::
    :question: What is ``cities[(37.7749, 122.4194)]``?
    :correct_answer: San Francisco
    :explanation: Correct answer is San Francisco
    :question_num: 1

.. free-response::
    :question: What is ``coordinates['Austin']``?
    :correct_answer: (30.2672, 97.7431)
    :explanation: Correct answer is (30.2672, 97.7431)
    :question_num: 2

.. free-response::
    :question: What is ``cities[(40.7128, 74.006)]``?
    :correct_answer: New York
    :explanation: Correct answer is New York
    :question_num: 3

.. free-response::
    :question: What is ``cities['San Diego']``?
    :correct_answer: KeyError
    :explanation: Correct answer is KeyError
    :question_num: 4