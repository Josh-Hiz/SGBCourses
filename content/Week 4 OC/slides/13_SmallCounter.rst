SmallCounter
============

Define a class ``SmallCounter`` that has methods ``tick``, ``untick``, and ``value``. The ``tick`` method should increment an internal field by 1; the ``untick`` method should decrement it by 1. The internal counter field should start 0. The value method return the current value.

Your ``SmallCounter`` should only ever be between 0 and 10. If someone calls ``untick`` when the counter is 0, it should stay at 0; if someone calls ``tick`` when the counter is 10, it should stay at 10.

.. challenge::
    :tester: /_static/cs515_challenges/Week5/Challenge3/test_task.py

    # define SmallCounter
