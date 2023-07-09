red_filter_pixel
================

Let's start by coding a red filter for a single pixel. Remember, pixels are given as a **3-tuple**, which is an **immutable** data structure. Meaning, you will need to generate a new tuple! Create a function called ``red_filter_pixel(px)`` which takes as an argument a **RGB 3-tuple** ``p`` and returns an **RGB 3-tuple** that has been red filtered, i.e., has non-red parts set to 0.

Here is a pixel with the color values (200,250,150):

.. image:: /assets/images/cs515/Week3/image_filter.png
    :align: center

And here it is after being red filtered, with colors values (200,0,0):

.. image:: /assets/images/cs515/Week3/image_red_filter.png
    :align: center

.. challenge::
    :tester: /_static/cs515_challenges/Week3/Challenge12/task.py

    # define red_filter_pixel(px)