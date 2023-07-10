Overwriting references
======================

.. quizdown::

    ### Consider the following code. Choose all that are correct after the code has been executed.

    Note: ```copy_img``` and ```img``` are local variables and cannot be accessed outside of the function. The question is asking whether the variables contained some reference to the same object at any point within the execution of the code.

    ```
    def make_copy(img):
        copy_img = []
        for row_idx in range(len(img)):
            row = []
            for col_idx in range(len(img[row_idx])):
                row.append(img[row_idx][col_idx])
            copy_img.append(row)
        return copy_img

    rgb_square = [[(255, 0, 0), (0, 255, 0), (0, 0, 255)],
                [(255, 0, 0), (0, 255, 0), (0, 0, 255)],
                [(255, 0, 0), (0, 255, 0), (0, 0, 255)]]
    rgb_square = make_copy(rgb_square)
    ```

    - [ ] img and copy_img referenced the same object.
    - [x] rgb_square and copy_img referenced the same object.
    - [x] rgb_square and img referenced the same object.