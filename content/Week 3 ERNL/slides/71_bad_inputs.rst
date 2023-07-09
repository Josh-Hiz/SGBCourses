Bad inputs
==========

.. quizdown::

    ### Given an image which is represented as a 2D list as follows:

    ```python
    img = [[(240, 240, 200), (200, 200, 100), (240, 240, 150), (200, 200, 125)], 
           [(160, 240, 120), (120, 200, 140), (160, 240, 240), (120, 200, 120)], 
           [(240, 240, 220), (200, 200, 210), (240, 240, 130), (200, 200, 140)], 
           [(160, 240, 110), (120, 200, 120), (160, 240, 120), (120, 200, 130)]]
    ```

    Based on the previous reading, which of the following inputs will cause either "Invalid input" or "Input parameter out of bounds" to be returned from the ```custom_red_filter``` function for the above image ```img```?

    - [ ] ```
        top_left = (0, 1)
        height = 4
        width = 3
        ```
    - [x] ```
        top_left = (-1, -1)
        height = 2
        width = 2
        ```
    - [x] ```
        top_left = (0, 1)
        height = -2
        width = -3
        ```
    - [x] ```
        top_left = (2, 1)
        height = 3
        width = 3
        ```
    - [x] ```
        top_left = (2,2)
        height = 2
        width = 3
        ``` 