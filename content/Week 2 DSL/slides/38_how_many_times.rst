How many times does it run?
===========================

.. quizdown:: 

    ## Trace through the code below and select how many times the body of the for loop within the ``multiply`` function runs and what value is returned for the function call ``multiply([10, 2, 0, 3])``

    ```python
    def multiply(lst):
        product = 1
        for a in lst:
            product = product * a
        return product
    ```

    - [ ] The loop runs for 1 iteration
    - [ ] The loop runs for 2 iterations
    - [ ] The loop runs for 3 iterations
    - [x] The loop runs for 4 iterations
    - [ ] The loop runs for 5 iterations
    - [x] The value returned is 0
    - [ ] The value returned is 1
    - [ ] The value returned is 15
    - [ ] The value returned is 16
    - [ ] The value returned is 60