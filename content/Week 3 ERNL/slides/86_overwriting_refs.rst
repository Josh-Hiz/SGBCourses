Overwriting references
======================

Now consider the following version of the previously shown code.

.. runner::

    def flip_left_right(img):
        # make a copy of img
        copy_img = []
        for row_idx in range(len(img)):
            row = []
            for col_idx in range(len(img[row_idx])):
                row.append(img[row_idx][col_idx])
            copy_img.append(row)
            
        # Flip copy_img over the y-axis
        for y in range(len(copy_img)):
            for x in range(len(copy_img[y]) // 2):
                temp = copy_img[y][x]
                copy_img[y][x] = copy_img[y][len(copy_img[y]) - x - 1]
                copy_img[y][len(copy_img[y]) - x - 1] = temp
        return copy_img

    rgb_square = [[(255, 0, 0), (0, 255, 0), (0, 0, 255)],
                [(255, 0, 0), (0, 255, 0), (0, 0, 255)],
                [(255, 0, 0), (0, 255, 0), (0, 0, 255)]]

    print("rgb_square before flip_left_right =", rgb_square)
    rgb_square = flip_left_right(rgb_square)
    print("rgb_square after flip_left_right =", rgb_square)

The above code outputs the following. Although we created and returned a copy of ``img``, ``rgb_square`` was still modified. What happened?

.. code-block::

    rgb_square before flip_left_right = [[(255, 0, 0), (0, 255, 0), (0, 0, 255)],
                                         [(255, 0, 0), (0, 255, 0), (0, 0, 255)],
                                         [(255, 0, 0), (0, 255, 0), (0, 0, 255)]]

    rgb_square after flip_left_right = [[(0, 0, 255), (0, 255, 0), (255, 0, 0)],
                                        [(0, 0, 255), (0, 255, 0), (255, 0, 0)],
                                        [(0, 0, 255), (0, 255, 0), (255, 0, 0)]]

Take a closer look at the following line.

.. code-block::

    rgb_square = flip_left_right(rgb_square)

Since we overwrote ``rgb_square`` with the returned value of the function ``flip_left_right``, we overwrote the initial reference that ``rgb_square`` contained. When ``flip_left_right`` was called, both ``rbg_square`` and ``img`` contained references to the same object. When we created and returned ``copy_img``, we returned the reference to the newly created object. We then stored this reference to ``rgb_square``. After the above line executes, ``rgb_square`` contains the reference to the new object instead of the previous object, the original ``rgb_square``.