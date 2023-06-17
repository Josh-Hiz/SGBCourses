News update
===========

Suppose we have the following dictionary:

.. code-block::
    
    fruit = { 'apples': 10, 'oranges': 15, 'pears': 12 }

We're going shopping, and we want to update the ``fruit`` dictionary to be:

.. code-block:: 

    fruit = { 'apples': 10, 'oranges': 15, 'pears': 12, 'bananas': 4, 'pineapple': 1 }

.. quizdown::

    # Which of the following will accomplish that?

    - [x] ``fruit.update({'bananas': 4, 'pineapple': 1})``
    - [ ] ``fruit.update({'bananas', 4, 'pineapple', 1)``
    - [ ] ``fruit.update(['bananas', 4, 'pineapple', 1])``
    - [x] ``fruit.update([('bananas', 4), ('pineapple', 1)])``
    - [ ] ``fruit.update('bananas', 4, 'pineapple', 1)``