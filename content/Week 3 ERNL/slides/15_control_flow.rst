Exceptional control flow, redux
===============================

.. quizdown:: 

    ### What will the following program output?

    ```python
    try:
        print('hello')
        raise ValueError('alas')
    except:
        print('oh no')
    ```

    1. [ ] ```hello```
    2. [ ] ```alas```
    3. [x] ```
    hello
    oh no```
    4. [ ] ```
    hello
    alas
    ``` 
    5. [ ] ```
    hello
    alas
    oh no
    ```

    ### What will the following program output?

    ```python
    try:
        print('hello')
        raise RuntimeError('alas')
    except ValueError:
        print('oh no')
    except:
        print('all the way')
    ```

    1. [ ] ```hello```
    2. [ ] ```alas```
    3. [ ] ```
    hello
    oh no
    ```
    4. [x] ```
    hello
    all the way
    ``` 
    5. [ ] ```
    hello
    oh no
    all the way
    ```

    ### What will the following program output?

    ```python
    def result(n):
        return 100/n

    try:
        print(result(20))
        print(result(0))
    except ValueError:
        print('zoiks')
    except ZeroDivisionError:
        print('yikes')
    ```

    1. [ ] ```5.0```
    2. [ ] ```
    5.0
    NaN
    ```
    3. [ ] ```
    5.0
    zoiks
    ```
    4. [x] ```
    5.0
    yikes
    ``` 
    5. [ ] ```
    5.0
    zoiks
    yikes
    ```