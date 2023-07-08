Exceptional control flow
========================

.. quizdown:: 

    ### What does the following code snippet output?

    ```python
    try:
        print('hello')
    except:
        print('goodbye')
    ```

    1. [x] ```hello```
    2. [ ] ```goodbye```
    3. [ ] ```
    hello
    goodbye
    ```
    4. [ ] No output


    ### What does the following code snippet output?

    ```python
    try:
        print('hello')
        x = 10 / 0
    except:
        print('goodbye')
    ```

    1. [ ] ```hello```
    2. [ ] ```goodbye```
    3. [x] ```
    hello
    goodbye
    ```
    4. [ ] No output


    ### What does the following code snippet output?

    ```python
    try:
        l = []
        print(l[0])
        print('hello')
    except:
        print('goodbye')
    ```

    1. [ ] ```hello```
    2. [x] ```goodbye```
    3. [ ] ```
    hello
    goodbye
    ```
    4. [ ] No output

    > Notice that the first ```print``` never outputs anything---the ```IndexError``` occurs before ```print``` even gets called, and we go straight to the exception handler.