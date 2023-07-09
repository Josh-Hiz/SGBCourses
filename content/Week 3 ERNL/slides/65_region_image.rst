Working in just a region of an image
====================================

We have learned that images displayed on digital screens comprise grids of pixels, where each pixel is associated with a color. Also, we have seen that the color information of pixels in images can be represented as 2D lists of tuples. You have also learnt how to handle images using nested for loops.

You have learnt how to apply a red filter to an entire image in the previous lesson. Now let us see how we can transform only a specified region of the image by applying a red filter on it.

The following 4X4 image is given as a 2D list called ``our_image``.

.. image:: /assets/images/cs515/Week3/image_region.png
    :align: center

The RGB values of the pixels are:

.. code-block::

    (240, 240, 0)     (200, 200, 0)     (240, 240, 0)     (200, 200, 0)
    (160, 240, 0)     (120, 200, 0)     (160, 240, 0)     (120, 200, 0)
    (240, 240, 0)     (200, 200, 0)     (240, 240, 0)     (200, 200, 0)
    (160, 240, 0)     (120, 200, 0)     (160, 240, 0)     (120, 200, 0)

Here is how ``our_image`` is shown in Python as a 2D List.

.. code-block::

    >>> our_image
    [[(240, 240, 0), (200, 200, 0), (240, 240, 0), (200, 200, 0)], [(160, 240, 0), (120, 200, 0), (160, 240, 0), 
    (120, 200, 0)], [(240, 240, 0), (200, 200, 0), (240, 240, 0), (200, 200, 0)], [(160, 240, 0), (120, 200, 0), 
    (160, 240, 0), (120, 200, 0)]]

Our goal is to transform the above image by applying the red filter to the center of the image only as shown below:

.. image:: /assets/images/cs515/Week3/image_region_2.png
    :align: center

The concept of applying the red filter is the same as described in the previous lesson. We need to **retain the red component of the corresponding pixel and make the blue and green components as 0**, but on only the specified region. We will specify the region with the help of three parameters:

* a tuple called ``top_left`` which specifies the row index followed by column index (in zero based indexing) of the top left corner of the region where the red filter needs to be applied
* an integer ``height`` that specifies the height of the region where the red filter needs to be applied
* an integer ``width`` that specifies the width of the region where the red filter needs to be applied.

For example, in the above figure, the value of ``top_left`` would be ``(1,1)`` since the region starts from row index 1 and column index 1 as per zero based indexing, the value of ``height`` would be 2 and the value of width would be 2 since the region spans two pixels in height and in width.

The RGB values of each pixel in the filtered image is as follows:

.. code-block::

    (240, 240, 0)     (200, 200, 0)     (240, 240, 0)     (200, 200, 0)
    (160, 240, 0)     (120, 0, 0)       (160, 0, 0)       (120, 200, 0)
    (240, 240, 0)     (200, 0, 0)       (240, 0, 0)       (200, 200, 0)
    (160, 240, 0)     (120, 200, 0)     (160, 240, 0)     (120, 200, 0)

As you can see above, applying the red filter means retaining only the red component of the pixel tuple and making the green and blur components as 0.

Here is how the filtered image is shown in Python as a 2D List.

.. code-block::

    [[(240, 240, 0), (200, 200, 0), (240, 240, 0), (200, 200, 0)], [(160, 240, 0), (120, 0, 0), (160, 0, 0), 
    (120, 200, 0)], [(240, 240, 0), (200, 0, 0), (240, 0, 0), (200, 200, 0)], [(160, 240, 0), (120, 200, 0), 
    (160, 240, 0), (120, 200, 0)]]