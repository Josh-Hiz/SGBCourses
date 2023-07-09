Using for loops
===============

Now, suppose we have a 3x3 grid of pixels that is represented by a 2D list. Let's suppose we take your ``red_filter_pixel()`` function, and apply it to each of the pixels in a 3x3 image. Which of the following **nested for loops** will properly produce the following result, assuming our 2D list is called ``img``?

Here's our initial ``img``:

.. code-block::

    (255,128,128) (5,100,200)   (255,128,128)
    (100,5,200)   (255,128,128) (100,5,200)
    (255,128,128) (5,100,200)   (255,128,128)

and here is it after having the **nested for loop** applied:

.. code-block::

    (255,0,0)   (5,0,0) (255,0,0)
    (100,0,0) (255,0,0) (100,0,0)
    (255,0,0)   (5,0,0) (255,0,0)

.. quizdown::

    ### Which loop will apply a red filter to ```img``` correctly?

    1. [ ] ```
        for i in range(len(img)):
            for j in range(len(img[i])):
                red_filter_pixel(img)
        ```
    2. [ ] ```
        for i in range(len(img)):
            for j in range(len(img[i])):
                img[i][j] = red_filter_pixel(j)
        ```
    3. [ ] ```
        for i in img:
            for j in i:
                pixel = img[i][j]
                red_filter_pixel(pixel)
        ```
    4. [x] ```
        for i in range(len(img)):
            for j in range(len(img[i])):
                img[i][j] = red_filter_pixel(img[i][j])
        ```