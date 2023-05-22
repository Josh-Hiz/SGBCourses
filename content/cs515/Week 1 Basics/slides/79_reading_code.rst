Reading Code
============

Remember a local variable that is created in a local scope cannot be accessed by the global scope or the other local scopes. 

.. code-block:: python

    def assign_x():
    x = 1
    modify_x()
    print(x)

    def modify_x():
        x = 2

    x = 0
    assign_x()

.. quizdown::

    ## What will this code print out?

    1. [ ] 0
    2. [x] 1
    3. [ ] 2
    4. [ ] Nothing