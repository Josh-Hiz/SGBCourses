Understanding objects and references
====================================

.. quizdown::

    ### As in the previous step, we run the following code.

    ```
    def flip_left_right(img):
        for y in range(len(img)):
            for x in range(len(img[y])//2):
                temp = img[y][x]
                img[y][x] = img[y][len(img[y])-x-1]
                img[y][len(img[y])-x-1] = temp
        return img

    rgb_square =[[(255,0,0),(0,255,0), (0,0,255)],
                [(255,0,0),(0,255,0), (0,0,255)],
                [(255,0,0),(0,255,0), (0,0,255)]]
    flipped = flip_left_right(rgb_square)
    ```

    After the above code is run, we edit rgb_square as follows.

    ```
    rgb_square[0][0] = (0, 0, 255)
    ```

    Now, which of the following options is ```True```?

    1. [x] ```id(rgb_square[0]) == id(flipped[0])```
    2. [ ] ```flipped[0][0] == (255, 0, 0)```
    3. [ ] ```id(rgb_square) != id(flipped)```
    4. [ ] ```flipped[0][0][0] == 255```
