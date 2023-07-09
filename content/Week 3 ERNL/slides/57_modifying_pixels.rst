Modifying pixels of an image
============================

We can access the color information of certain columns of images in a similar way. We still have the 3X4 image saved as a 2D list ``our_image``.

.. image:: /assets/images/cs515/Week3/rows.png
    :align: center

The RGB values of each pixel is as follows:

.. code-block::

    (0,0,0)   (0,80,0)   (0,160,0)   (0,240,0)
    (120,0,0) (120,80,0) (120,160,0) (120,240,0)
    (240,0,0) (240,80,0) (240,160,0) (240,240,0)

Suppose we want to change this. Say you really like the color blue and you want the B component of every pixel to be the maximum value 255. Before writing a complete program, let's handle a single pixel at the leftmost row and the top column, which is ``our_image[0][0]``. We have learned before that the B component of this pixel can be accessed by ``our_image[0][0][2]``.

.. code-block::

    >>> our_image[0][0][2]
    0

So why don't we just run ``our_image[0][0][2] = 255``? This is what would happen:

.. code-block::

    >>> our_image[0][0][2] = 255
    Traceback (most recent call last):
        File "<pyshell#10>", line 1, in <module>
            our_image[0][0][2] = 255
    TypeError: 'tuple' object does not support item assignment

It is impossible to mutate an element of a tuple because tuples are immutable. Then, how can we modify a pixel without mutating a tuple? We can't modify a tuple, but we CAN reassign the pixel with a new tuple, because this is not against the rule.

.. code-block::

    our_image[0][0] = (0,0,225)

Implementing this way, we did not try modifying the tuple ``(0,0,0)``, but we just reassigned a new tuple ``(0,0,225)`` to the pixel. Now, the RGB values and the image are changed as follows:

.. code-block::

    (0,0,255) (0,80,0)   (0,160,0)   (0,240,0)
    (120,0,0) (120,80,0) (120,160,0) (120,240,0)
    (240,0,0) (240,80,0) (240,160,0) (240,240,0)