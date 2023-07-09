Nested for loops to access images
==================================

We can access the color information of certain columns of images in a similar way. We still have the 3X4 image saved as a 2D list ``our_image``.

.. image:: /assets/images/cs515/Week3/rows.png
    :align: center

The RGB values of each pixel is as follows:

.. code-block::

    (0,0,0)   (0,80,0)   (0,160,0)   (0,240,0)
    (120,0,0) (120,80,0) (120,160,0) (120,240,0)
    (240,0,0) (240,80,0) (240,160,0) (240,240,0)

Using tricks we've learned so far, we can output each column by copy/pasting code:

.. code-block::

    for column in range(4):
        print(our_image[1][column])

    for column in range(4):
        print(our_image[2][column])

which leads to

.. code-block::

    (120,0,0)
    (120,80,0)
    (120,160,0)
    (120,240,0)
    (240,0,0)
    (240,80,0)
    (240,160,0)
    (240,240,0)

as we wanted. However, nested ``for`` loops can generate the same result with more concise code as follows:

.. code-block::

    for row in range(1,3):
        for column in range(4):
            print(our_image[row][column])

Here are the details of how the nested ``for`` loops printed the desired result.

* ``row`` is ``1`` at the initial iteration of the outer ``for`` loop 
    * ``column`` is ``0`` at the initial iteration of the inner ``for`` loop
    * ``our_image[1][0]`` is printed
    * ``column`` is ``1`` at the next iteration of the inner ``for`` loop
    * ``our_image[1][1]`` is printed
    * ``column`` is ``2`` at the next iteration of the inner ``for`` loop
    * ``our_image[1][2]`` is printed
    * ``column`` is ``3`` at the next iteration of the inner ``for`` loop
    * ``our_image[1][3]`` is printed
* ``row`` is ``2`` at the next iteration of the outer ``for`` loop 
    * ``column`` is ``0`` at the initial iteration of the inner ``for`` loop
    * ``our_image[2][0]`` is printed
    * ``column`` is ``1`` at the next iteration of the inner ``for`` loop
    * ``our_image[2][1]`` is printed
    * ``column`` is ``2`` at the next iteration of the inner ``for`` loop
    * ``our_image[2][2]`` is printed
    * ``column`` is ``3`` at the next iteration of the inner ``for`` loop
    * ``our_image[2][3]`` is printed

Similarly, we can print the information of the entire image!

.. code-block::

    for row in range(3):
        for column in range(4):
            print(our_image[row][column])
    
Here is the output.

.. code-block::

    (0,0,0)
    (0,80,0)
    (0,160,0)
    (0,240,0)
    (120,0,0)
    (120,80,0)
    (120,160,0)
    (120,240,0)
    (240,0,0)
    (240,80,0)
    (240,160,0)
    (240,240,0)

You can be assured that the correct information is printed according to the RGB table of the image above.