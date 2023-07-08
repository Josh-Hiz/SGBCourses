Identifying the parts
=====================

.. quizdown::

    ### What is the base case of this function?

    ```
    def f(l):
        if len(l) == 0:
            return 0
        else:
            l[0] + f(l[1:])
    ```

    1. [x] ```
    if len(l) == 0:
        return 0
    ```
    2. [ ] ```f(l[1:])```
    3. [ ] ```l[0] + f(l[1:])```
    4. [ ] ```
    else:
        l[0] + f(l[1:])
    ```

    ### Which are the base-cases of the following function?

    ```
    def g(l):
        if len(l) == 0:
            return 0
        elif len(l) == 1:
            return l[0]
        else:
            mid = len(l)//2
            return g(l[:mid]) + g(l[mid:])
    ```

    - [x] ```
    if len(l) == 0:
        return 0
    ```
    - [x] ```
    elif len(l) == 1:
        return l[0]
    ```
    - [ ] ```
    else:
        mid = len(l)//2
        return g(l[:mid]) + g(l[mid:])
    ```
    - [ ] There are no base cases

    ### Which are the recursive-cases of the following function?

    ```
    def h(s):
        if s.isupper():
            return True
        elif s.islower():
            return True
        else:
            return len(s.split('\n')) + 1
    ```

    - [ ] ```
    if s.isupper():
        return True
    ```
    - [ ] ```
    elif s.islower():
        return True
        ```
    - [x] ```
    else:
        return len(s.split('\n')) + 1
    ```
    - [ ] There are no recursive cases

    > ```h``` isn't a recursive function---it doesn't call itself! All three cases are base cases and none are recursive.


