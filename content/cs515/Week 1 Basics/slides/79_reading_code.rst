Reading Code
============

.. quizdown::

    ## What will this code print out?

    ```python
    def assign_x():
        x = 1
        modify_x()
        print(x)

    def modify_x():
        x = 2

    x = 0
    assign_x()
    ```

    1. [ ] 0
    2. [x] 1
    3. [ ] 2
    4. [ ] Nothing

    ## What about this code?

    ```python
    def assign_x():
        x = 1
        increase_x()
        print(x)

    def increase_x():
        x = x + 1
        return x
    
    x = 0
    assign_x()
    ```

    1. [ ] 0
    2. [x] 1
    3. [ ] 2
    4. [ ] Nothing

    ## What about this code?

    ```python
    def assign_x():
        x = 1
        x = increase_x(x)
        print(x)

    def increase_x(x):
        x = x + 1
        return x

    x = 0
    assign_x()
    ```

    1. [ ] 0
    2. [ ] 1
    3. [x] 2
    4. [ ] Nothing

    ## How many times is `'local_2'` printed by this code?

    ```python
    def local_1():
        x = 'local_1'
        print(x)

    def local_2():
        x = 'local_2'
        print(x)
        local_1()
        print(x)

    x = 'global'
    local_2()
    print(x)
    ```

    1. [ ] 1
    2. [x] 2
    3. [ ] 3
    4. [ ] 4