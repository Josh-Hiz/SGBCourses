We're all tired at this point in the semester
=============================================

.. quizdown::

    ### Oh no: a student who fell asleep when reading about swapping. They wrote the following invalid code.

    ```
    for y in range(len(img)):
        for x in range(len(img[y])//2):
            img[y][x] = img[y][len(img[y])-x-1]
            img[y][len(img[y])-x-1] = img[y][x]
    ```
    
    What will happen if we use this code?

    1. [ ] The flipped version of the left half of ``img`` will be assigned to the right-half
    2. [ ] The left half of the ``img`` will be blacked out
    3. [x] The flipped version of the right half of ``img`` will be assigned to the left-half
    4. [ ] The right half of the ``img`` will be removed