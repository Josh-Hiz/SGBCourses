More simulation
===============

.. quizdown::

    ### Choose the correct output for the code snippet below:
    
    ```python
    lst1 = ["0", "1", "2", "3"]
    lst2 = ["0", "1", "2", "3", "4"]
    result = ""
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            result += lst1[i] + lst2[j] + " "

    print(result)
    ```

    1. [ ] ```01 12 23 34```
    2. [ ] ```10 21 32 43```
    3. [x] ```00 01 02 03 04 10 11 12 13 14 20 21 22 23 24 30 31 32 33 34```
    4. [ ] ```00 10 20 30 40 01 11 21 31 41 02 12 22 32 42 03 13 23 33 43``` 