Apply a red filter to an image
==============================

At this point, we should have a fairly solid grasp on how we can store images in 2D lists and how we can use nested for loops to manipulate them. Let's apply our knowledge to a practical problem. Suppose we have an RGB image and we want to apply a red filter such that only the red component of each pixel is present in our output image. For example:

.. image:: /assets/images/cs515/Week3/owl.jpg
    :align: center

What a cute owl! (It's a `tawny owl <https://en.wikipedia.org/wiki/Tawny_owl>`_.) Let's see what displaying only the red component of each pixel in this image will look like.

.. image:: /assets/images/cs515/Week3/image.png
    :align: center

The owl is a little scarier looking (happy Halloween), but lovable all the same. This image is fairly high resolution, but thanks to the magic of for loops, we can create a general solution that will work with images of any size. So how do we go about creating a solution? Let's start by thinking about a single pixel. Recall that a single pixel is a **3-tuple** of the form (R, G, B), where R, G and B are integers between 0 and 255 that represent the intensity of a given color: red, green, and blue, respectively. When we apply a **red filter**, we want only the red component of this **3-tuple** to remain. So, (R, G, B) becomes (R, 0, 0). In other words, we set G and B (green and blue) to 0, and keep the red value the same. Let's start with a single pixel.