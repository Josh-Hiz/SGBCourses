Copying and flipping
====================

We saw earlier that modifying the 2D list image in the function modified ``rgb_square``. We can solve this by making a copy of the image and returning the copy.

Below is the modified version of ``flip_left_right``. Notice that we have changed the function to first make a copy of ``img``. Instead of modifying ``img``, we modified ``copy_img`` and returned ``copy_img`` which will prevent our original ``img`` from being modified.

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
            for x in range(len(copy_img[y]) // 2): # Recall the integer division
                temp = copy_img[y][x]
                copy_img[y][x] = copy_img[y][len(copy_img[y]) - x - 1]
                copy_img[y][len(copy_img[y]) - x - 1] = temp
        return copy_img

    rgb_square = [[(255, 0, 0), (0, 255, 0), (0, 0, 255)],
                [(255, 0, 0), (0, 255, 0), (0, 0, 255)],
                [(255, 0, 0), (0, 255, 0), (0, 0, 255)]]

    print("rbg_square before flip_left_right =", rgb_square)
    rgb_square_flipped = flip_left_right(rgb_square)
    print("rbg_square after flip_left_right =", rgb_square)
    print("rbg_square_flipped =", rgb_square_flipped)

Our updated code prints the following. Notice that the argument, ``rgb_square``, remained the same after we called the function and the new variable, ``rgb_square_flipped``, stores the return of ``flip_left_right(rgb_square)``.

.. code-block::

    rgb_square before flip_left_right = [[(255, 0, 0), (0, 255, 0), (0, 0, 255)],
                                        [(255, 0, 0), (0, 255, 0), (0, 0, 255)],
                                        [(255, 0, 0), (0, 255, 0), (0, 0, 255)]]
    rgb_square after flip_left_right = [[(255, 0, 0), (0, 255, 0), (0, 0, 255)],
                                        [(255, 0, 0), (0, 255, 0), (0, 0, 255)],
                                        [(255, 0, 0), (0, 255, 0), (0, 0, 255)]]
    rbg_square_flipped = [[(0, 0, 255), (0, 255, 0), (255, 0, 0)],
                        [(0, 0, 255), (0, 255, 0), (255, 0, 0)],
                        [(0, 0, 255), (0, 255, 0), (255, 0, 0)]]

Why did this work? In the previous lesson, we learned that ``img`` and ``rgb_square`` are actually references to the same object. By creating a copy of ``img``, we have created a new 2d list object that contains the same elements as ``img``. Now, ``copy_img`` references this new object. When we return ``copy_img``, ``rgb_square_flipped`` will contain the same reference as ``copy_img``; hence, ``rbg_square_flipped`` will reference the new object that was created in the function. 

Keep in mind that ``copy_img`` and ``img`` are local variables to ``flip_left_right`` and only exist within the function. We cannot access ``copy_img`` and ``img`` outside of ``flip_left_right``.

Optimization: copy on-the-fly
-----------------------------

Our code above copies and then flips. We could work differently, copying on the fly:

.. runner::

    def flip_left_right(img):       
        copy_img = [] # an empty image
        for y in range(len(img)):
            copy_img.append([]) # make an empty row
            for x in range(len(img[y])): # loop through _everything_
                copy_img[y].append(img[y][len(img[y]) - x - 1]) # copy in from img
        return copy_img

    rgb_square = [[(255, 0, 0), (0, 255, 0), (0, 0, 255)],
                [(255, 0, 0), (0, 255, 0), (0, 0, 255)],
                [(255, 0, 0), (0, 255, 0), (0, 0, 255)]]

    print("rbg_square before flip_left_right =", rgb_square)
    rgb_square_flipped = flip_left_right(rgb_square)
    print("rbg_square after flip_left_right =", rgb_square)
    print("rbg_square_flipped =", rgb_square_flipped)

Notice how we avoid a lot of work: we don't have to initialize ``copy_img`` up front; we don't have to worry about temporary variables or stopping in the middle. It's often much easier to write copying code than to do things in place!