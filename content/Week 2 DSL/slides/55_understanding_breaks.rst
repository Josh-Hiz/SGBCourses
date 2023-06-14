Understanding for loop with breaks
==================================

.. quizdown:: 

    ### Here is the code with a ``for`` loop and a ``break`` statement that counts numbers in a list until zero appears as a stop sign. The variable ``count`` is initialized to 0 and is incremented by 1 every time the ``for`` loop has a non-zero number until the ``break`` statement is implemented. What is the final value of ``count`` that will be printed?

    ```python
    num_list = [-25, -12, 3.7, 5.2, 0, 2, 4.5, 0, 1]
    count = 0
    for num in num_list:
        if num == 0:
            break
        count = count + 1
    print(count)
    ```

    1. [x] 4
    2. [ ] 8
    3. [ ] 6
    4. [ ] 2
