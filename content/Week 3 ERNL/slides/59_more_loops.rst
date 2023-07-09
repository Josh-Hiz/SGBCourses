More for loops
==============

We can access the color information of certain columns of images in a similar way. We still have the 3X4 image saved as a 2D list ``our_image``.

.. image:: /assets/images/cs515/Week3/rows.png
    :align: center

The RGB values of each pixel is as follows:

.. code-block::

    (0,0,0)   (0,80,0)   (0,160,0)   (0,240,0)
    (120,0,0) (120,80,0) (120,160,0) (120,240,0)
    (240,0,0) (240,80,0) (240,160,0) (240,240,0)

Let's change all of the pixels. Assume that your favorite color is now green. So you want to make the R components of every pixel be 0. As a baby step, let's bring back the code from step 5, which travels over every pixel of the image. 

.. code-block::

    for row in range(3):
        for column in range(4):
            print(our_image[row][column])

Here, we can apply the strategy from the previous step as follows:

.. code-block::

    for row in range(3):
        for column in range(4):
            temp_pixel = our_image[row][column]

For each iteration, we would like to make a new tuple ``(0, temp_pixel[1], temp_pixel[2])``, as we want to make the R component 0. Thus, the code is completed as

.. code-block::

    for row in range(3):
        for column in range(4):
            temp_pixel = our_image[row][column]
            our_image[row][column] = (0, temp_pixel[1], temp_pixel[2])

Then, the components become:

.. code-block::

    (0,0,0) (0,80,0) (0,160,0) (0,240,0)
    (0,0,0) (0,80,0) (0,160,0) (0,240,0)
    (0,0,0) (0,80,0) (0,160,0) (0,240,0)

.. image:: /assets/images/cs515/Week3/rows_green.png
    :align: center