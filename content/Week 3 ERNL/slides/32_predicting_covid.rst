Predicting COVID cases
======================

A researcher at UC San Diego Health now wants to predict COVID-19 cases in the next few days! 

She has a list ``cases`` which contains the current number of cases in San Francisco, Santa Barbara, Los Angeles, and San Diego.

.. code-block::

    cases = [12508, 9969, 310595, 57409]

She also has a list ``predicted_growths`` which contains the predicted number of new cases for every ``city`` in the next few days. 

For example: 

Suppose today is 11/02/2020, 

.. code-block::

    predicted_growths = [100, 200, 300]

which means that the predicted number of new cases on **11/03/2020 is 100** for **every** city, the predicted number of new cases on **11/04/2020 is 200** and the predicted number of new cases on **11/05/2020 is 300**.

**Your job:** Define a function ``predict(cases, predicted_growths)`` using nested for-loops, help the researcher print out the predicted number of **all cases** for each city in the next ``k`` days, where ``k`` is the length of ``predicted_growths``. Note: you can assume that ``cases`` and ``predicted_growths`` are lists, and that ``k == len(predicted_growths) > 0``. It's okay to update ``cases``.

**Sample 1:** 

.. code-block::

    cases = [12508, 9969, 310595, 57409]
    predicted_growths = [100, 200, 300]

You should print:

.. code-block::

    [12608, 10069, 310695, 57509]
    [12808, 10269, 310895, 57709]
    [13108, 10569, 311195, 58009]

**Sample 2:**

.. code-block::

    cases = [12508, 9969, 310595, 57409]
    predicted_growths = [1000, 2000, 3000, 4000]

You should print:

.. code-block::

    [13508, 10969, 311595, 58409]
    [15508, 12969, 313595, 60409]
    [18508, 15969, 316595, 63409]
    [22508, 19969, 320595, 67409]

**Sample 3:**

.. code-block::

    cases = [12508, 9969, 310595, 57409]
    predicted_growths = [10000]

You should print:

.. code-block::

    [22508, 19969, 320595, 67409]

.. challenge::
    :tester: /_static/cs515_challenges/Week3/Challenge4/test_task.py

    # define predict(cases, predicted_growths)