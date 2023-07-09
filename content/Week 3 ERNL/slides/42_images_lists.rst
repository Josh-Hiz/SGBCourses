Images and 2D lists
===================

In the last step, we learned that images are represented as grids of pixels. In Python, we can represent this grid of pixels as a 2D list. We have learned about 2D lists in the previous lessons.

Below is the same image from the previous step showing the coordinates of each pixel. Notice that coordinate (0,0) is the top left pixel and coordinates increase in value as you move from the top of a row to the bottom. This is different from how you may have visualized grids on a Cartesian plane.

.. image:: /assets/images/cs515/Week3/image_coord.PNG
    :align: center

To represent this image as a 2D list of pixels, we can create a list of rows and each row is a list of pixels. We will discuss representing pixels in a later step. For now, let's represent a pixel by P(coordinate) such that the pixel at coordinate (1,0) is P(1,0). This is called "row/column ordering", because the row comes before the column.

Below is a table representing the pixels of an image with a height of 3 and a width of 5 (not the image above).

.. code-block::

    P(0,0) P(0,1) P(0,2) P(0,3) P(0,4)
    P(1,0) P(1,1) P(1,2) P(1,3) P(1,4)
    P(2,0) P(2,1) P(2,2) P(2,3) P(2,4)

Now we can create a 2D list to represent this image. Notice that each element in the initial list is a list of pixels and each of these sub list of pixels represents a row of the image.

.. code-block::

    [[P(0,0), P(0,1), P(0,2), P(0,3), P(0,4)], 
    [P(1,0), P(1,1), P(1,2), P(1,3), P(1,4)], 
    [P(2,0), P(2,1), P(2,2), P(2,3), P(2,4)]]