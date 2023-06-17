Dictionaries within dictionaries
================================

.. code-block:: 

    states = {"California" : {"population" : 39512223, "capital" : "Sacramento", "landlocked" : False},
              "Oregon" : {"population" : 4217737, "capital" : "Salem", "landlocked" : False},
              "Nevada" : {"population" : 3080156, "capital" : "Carson City", "landlocked" : True}}

Let's get a bit of practice. Using the ``states`` dictionary above, give the output for each code snippet.

In case of a KeyError, give the key that was missing, i.e., ``KeyError: 'foo'``.

.. add-css::

.. free-response::
    :question: <code>states['California']['population']</code>
    :correct_answer: 39512223
    :explanation: Correct answer is 39512223
    :question_num: 1

.. free-response::
    :question: <code>states['Oregon']['capital']</code>
    :correct_answer: "Salem"
    :explanation: Correct answer is "Salem", 'Salem' would also be accurate
    :question_num: 2

.. free-response::
    :question: <code>states["Nevada"]["landlocked"] or states["Oregon"]["landlocked"]</code>
    :correct_answer: True
    :explanation: Correct answer is True
    :question_num: 3

.. free-response::
    :question: <code>states["California"]["landlocked"]</code>
    :correct_answer: False
    :explanation: Correct answer is False
    :question_num: 4

.. free-response::
    :question: <code>states['capital']['California']</code>
    :correct_answer: KeyError: "capital"
    :explanation: Correct answer is KeyError: "capital"
    :question_num: 5

.. free-response::
    :question: <code>states["Connecticut"]["population"]</code>
    :correct_answer: KeyError: "Connecticut"
    :explanation: Correct answer is KeyError: "Connecticut"
    :question_num: 6

.. free-response::
    :question: <code>states['Oregon']['area']</code>
    :correct_answer: KeyError: "area"
    :explanation: Correct answer is KeyError: "area"
    :question_num: 7

.. free-response::
    :question: <code>states['Nevada']['population']</code>
    :correct_answer: 3080156
    :explanation: Correct answer is 3080156
    :question_num: 8

.. free-response::
    :question: <code>states['Nevada']['capital']</code>
    :correct_answer: "Carson City"
    :explanation: Correct answer is "Carson City"
    :question_num: 9