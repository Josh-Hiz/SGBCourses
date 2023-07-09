More of a flop than a flip
==========================

.. quizdown::

    ### We have learned in the previous step that the following code flips ```img``` left to right.

    ```
    for y in range(len(img)):
        for x in range(len(img[y])//2):
            temp = img[y][x]
            img[y][x] = img[y][len(img[y])-x-1]
            img[y][len(img[y])-x-1] = temp
    ```

    However, one student wrote a slightly different code.

    ```
    for y in range(len(img)):
        for x in range(len(img[y])):
            temp = img[y][x]
            img[y][x] = img[y][len(img[y])-x-1]
            img[y][len(img[y])-x-1] = temp
    ```

    What will be the outcome if we use this code?

    1. [ ] ```img``` changes size
    2. [ ] ```img``` is flipped horizontally
    3. [ ] ```IndexError```
    4. [ ] ```img``` doesn't change at all