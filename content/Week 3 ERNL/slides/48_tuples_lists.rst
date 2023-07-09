Tuples and 2D lists
===================

Now that we can represent colors using tuples, we can use both tuples and 2D lists to represent a full image. Let's create the 2D list of tuples to represent the image below with a height of 3 and a width of 5.

.. image:: /assets/images/cs515/Week3/checkerboard.png
    :align: center

In step 2, we saw that the corresponding 2D list of an image with a height of 3 and a width of 5 would be the following. P(coordinate) is the pixel at that particular coordinate.

.. code-block::

    [[P(0,0), P(0,1), P(0,2), P(0,3), P(0,4)], 
    [P(1,0), P(1,1), P(1,2), P(1,3), P(1,4)], 
    [P(2,0), P(2,1), P(2,2), P(2,3), P(2,4)]]

We can then replace all P(coordinate) with the color at that particular pixel. Recall from the previous steps that the tuple, (255, 255, 255), is white and (0,0,0) is black. Our resulting 2D list of tuples would be the following. (We've added spaces so that things line up; they don't do anything other than make things more readable.)

.. code-block::

    [(0,0,0),       (255,255,255), (0,0,0),       (255,255,255), (0,0,0)], 
    [(255,255,255), (0,0,0),       (255,255,255), (0,0,0),       (255,255,255)], 
    [(0,0,0),       (255,255,255), (0,0,0),       (255,255,255), (0,0,0)]

Since the pixel at coordinate (0,0) is black, we replaced P(0,0) with (0,0,0). Moving on, we replaced P(0,1) to (255,255,255) because the pixel at coordinate (0,1) is white. We repeated these steps for all pixels to create the resulting 2D list of tuples.