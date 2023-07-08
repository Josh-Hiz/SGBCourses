Simulating nested for loops
===========================

.. quizdown::

    ### What is the output of the following code?

    ```python
    cases = [12508, 9969, 310595, 57409]
    n = 3
    for i in range(n):
        sum = 0
        for j in range(len(cases)):
            sum += cases[j]
        print('sum is: ' + str(sum))
    ```

    1. [ ] ```sum is: 390481```
    2. [ ] ```sum is: 390481```
    3. [x] ```
    sum is: 390481
    sum is: 390481
    sum is: 390481
    ```
    4. [ ] ```
    390481
    390481
    390481
    ```