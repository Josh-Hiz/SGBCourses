What kind of error?
===================

.. quizdown:: 

    ### Consider the following program:

    ```
    def mean(l):
        return sum(l) / len(l)
    
    print(mean([1,2,3]))
    print(mean([]))
    ```
    
    What error does it produce, if any?

    1. [ ] Syntax error
    2. [ ] ```NameError```
    3. [ ] ```TypeError```
    4. [x] ```ZeroDivisionError```
    5. [ ] ```IndexError```
    6. [ ] There are no errors

    ### Consider the following program:

    ```
    def mean(l):
        return sum(l) / len(l)

    print(mean(list(map(int, input().split()))))
    ```

    Which of the following errors could this program produce?

    - [ ] Syntax error
    - [ ] ```NameError```
    - [ ] ```TypeError```
    - [x] ```ZeroDivisionError```
    - [x] ```ValueError```
    - [ ] There are no errors

    > Giving an empty input will yield a ```ZeroDivisionError```; giving something other than numbers will yield a ```ValueError```.


    ### Consider the following program:

    ```
    def split(l):
        l1 = l[0:len(l)/2]
        l2 = l[len(l)/2:]
        return [l1, l2]
        
    print(split([]))
    ```

    What error does it produce?

    1. [ ] Syntax error
    2. [ ] ```NameError```
    3. [x] ```TypeError```
    4. [ ] ```IndexError```
    5. [ ] There are no errors

    > The division yields a ```float```, which slicing doesn't support.

    ### Consider the following program:

    ```
    def split(l):
        l1 = l[0:len(l)//2]
        l2 = l[len(l)//2:]
        return [l1, l2]
        
    print(split([]))
    ```

    What error does it produce?

    1. [ ] Syntax error
    2. [ ] ```NameError```
    3. [x] ```TypeError```
    4. [ ] ```IndexError```
    5. [ ] There are no errors

    > It's possible to get a ```TypeError``` by giving ```split``` a bad input---but this program has no errors.