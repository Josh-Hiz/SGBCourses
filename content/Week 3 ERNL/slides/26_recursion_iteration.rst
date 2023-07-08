Recursion into iteration (and vice versa) 
=========================================

Given a recursive program, we ask you to pick the equivalent iterative one (and vice versa).

.. quizdown::

    ### Which recursive function is equivalent?

    ```
    def f(l):
        total = 0
        for x in l:
            total += x
        return total
    ```

    1. [ ] ```
        def f(l):
            return l[0] + f(l[1:])
        ```
    2. [ ] ```
        def f(l):
            if len(l) == 0:
                return 0
            else:
                return l
        ```
    3. [ ] ```
        def f(l):
            if len(l) == 0:
                return 0
            else:
                return l[0] + f(l)
        ```
    4. [x] ```
        def f(l):
            if len(l) == 0:
                return 0
            else:
                return l[0] + f(l[1:])
        ```

    ### Which recursive function is equivalent?

    ```
    def hotpo(n):
        if n == 1:
            return
        elif n % 2 == 0:
            return hotpo(n // 2)
        else:
            return hotpo(n*3 + 1)
    ```

    1. [ ] ```
        def f(l):
            return l[0] + f(l[1:])
        ```
    2. [ ] ```
        def f(l):
            if len(l) == 0:
                return 0
            else:
                return l
        ```
    3. [ ] ```
        def f(l):
            if len(l) == 0:
                return 0
            else:
                return l[0] + f(l)
        ```
    4. [x] ```
        def f(l):
            if len(l) == 0:
                return 0
            else:   
                return l[0] + f(l[1:])
        ```