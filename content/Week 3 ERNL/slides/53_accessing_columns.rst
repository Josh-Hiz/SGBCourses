Accessing columns of images
===========================

We can access the color information of certain columns of images in a similar way. We still have the 3X4 image saved as a 2D list ``our_image``.

.. image:: /assets/images/cs515/Week3/rows.png
    :align: center

The RGB values of each pixel is as follows:

.. code-block::

    (0,0,0)   (0,80,0)   (0,160,0)   (0,240,0)
    (120,0,0) (120,80,0) (120,160,0) (120,240,0)
    (240,0,0) (240,80,0) (240,160,0) (240,240,0)

Now, your second favorite color is green, and you would like to print the values of the rightmost column, which has pixels of highest G components. The coordinates you want to access this case are (0,3),(1,3),(2,3). You are able to print the RGB values simply using ``print()`` multiple times as

.. code-block::

    print(our_image[0][3])
    print(our_image[1][3])
    print(our_image[2][3])

which prints the following output.

.. code-block::

    (0, 240, 0)
    (120, 240, 0)
    (240, 240, 0)

However, instead of manually repeating to type ``print()`` multiple times, we can use a ``for`` loop.

.. code-block::

    for row in range(3):
        print(our_image[row][3])

Now that we are dealing with the fixed column at index 3, the second index of ``our_image`` is set to 3. The variable ``row`` takes values among ``0,1,2`` for each iteration of the loop so that every pixel in that rightmost column can be handled. This code results in the same outcome as we wanted.

.. code-block::

    (0, 240, 0)
    (120, 240, 0)
    (240, 240, 0)