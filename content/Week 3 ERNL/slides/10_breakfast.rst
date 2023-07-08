Breakfast
=========

The following code simulates breakfast (you remember something similar from week 4). We've added a global variable ``bread`` that keeps track of how much bread you have left; you try to ``toast_bread`` without any bread, you'll get an exception.

.. runner:: 

    bread = 0

    def make_breakfast():
        fry_eggs()
        toast_bread()

    def fry_eggs():
        print("Sizzle sizzle")
        return

    def buy_bread():
        global bread
        bread = bread + 10

    def toast_bread():
        if bread <= 0:
            raise ValueError("out of bread")

        wait_for_toaster()
        return

    def wait_for_toaster():
        print("Ding ding!")
        return

    make_breakfast()

.. quizdown:: 

    ### Which functions are on the stack when the exception is raised?

    - [x] ```make_breakfast``` 
    - [ ] ```fry_eggs``` 
    - [ ] ```buy_bread``` 
    - [x] ```toast_bread```
    - [ ] ```wait_for_toaster```


    ### Which functions have been called at some point in the program when the exception is raised?

    - [x] ```make_breakfast``` 
    - [x] ```fry_eggs``` 
    - [ ] ```buy_bread``` 
    - [x] ```toast_bread```
    - [ ] ```wait_for_toaster```

    ### Suppose you were to fix this program by adding an exception handler of the following form:

    ```python
    try:
        # ... some existing code ...
    except:
        buy_bread()
        # ... some function call ...
    ```

    Where could you put this code and get the program to work? That is, the program should be unaltered except for the new handler, and the output should be:

    ```
    Sizzle, sizzle
    Ding ding!
    ```

    - [x] ```make_breakfast``` 
    - [ ] ```fry_eggs``` 
    - [ ] ```buy_bread``` 
    - [x] ```toast_bread```
    - [ ] ```wait_for_toaster```
    - [ ] Top-level call to ```make_breakfast```