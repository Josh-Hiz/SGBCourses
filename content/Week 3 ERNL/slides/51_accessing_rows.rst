Accessing rows of images
========================

We have learned that images displayed on digital screens comprise grids of pixels, where each pixel is associated with a single color. Also, we have seen that the color information of pixels in images can be represented as 2D lists of tuples. From now, we will cover how to handle images using ``for`` loops. 

The following 3X4 image is given as a 2D list ``our_image``.

.. image:: /assets/images/cs515/Week3/rows.png
    :align: center

The value of each RGB pixel is as follows:

.. code-block::

    (0,0,0)   (0,80,0)   (0,160,0)   (0,240,0)
    (120,0,0) (120,80,0) (120,160,0) (120,240,0)
    (240,0,0) (240,80,0) (240,160,0) (240,240,0)

Here is how ``our_image`` is shown in Python.

.. code-block::

    >>> our_image
    [[(0, 0, 0), (0, 80, 0), (0, 160, 0), (0, 240, 0)], 
    [(120, 0, 0), (120, 80, 0), (120, 160, 0), (120, 240, 0)], 
    [(240, 0, 0), (240, 80, 0), (240, 160, 0), (240, 240, 0)]]

As you may have guessed from the table of the pixel values, the R component of ``our_image`` increases by 120 from the top row to the bottom row, and the G component increases by 80 from the leftmost column to the rightmost column. And the B component is 0 for every pixel.

Now, your favorite color is red, and you would like to print the values of the bottom row, as that row has highest R components. Then, the coordinates you want to access are (2,0), (2,1), (2,2), (2,3). You may print the RGB values by just using ``print()`` multiple times as

.. code-block::

    print(our_image[2][0])
    print(our_image[2][1])
    print(our_image[2][2])
    print(our_image[2][3])

which prints the following output.

.. code-block::

    (240, 0, 0)
    (240, 80, 0)
    (240, 160, 0)
    (240, 240, 0)

However, instead of manually repeating to type ``print()`` multiple times, we can use a ``for`` loop.

.. code-block::

    for column in range(4):
        print(our_image[2][column])

Since we are dealing with the bottom row, the first index of ``our_image`` is set to 2. The variable ``column`` takes values among ``0,1,2,3`` for each iteration of the loop so that every pixel in that row can be handled in turn. This code results in the same outcome as follows:

.. code-block::

    (240, 0, 0)
    (240, 80, 0)
    (240, 160, 0)
    (240, 240, 0)

Imagine we have a 1000x1000 image. It's much better to write a 2-line ``for`` loop instead of typing ``print()`` 1000 times! 