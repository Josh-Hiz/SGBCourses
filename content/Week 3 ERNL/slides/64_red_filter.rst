Red filter
==========

Let's put it all together to create a general solution to the red filter problem. We can generalize the length of the nested for loops to the dimensions of the image, and red filter every pixel in the image by traversing the whole image with these nested for loops. We could write something like this:

.. runner::

    def red_filter(img):
        for row in range(len(img)):
            for col in range(len(img[0])):
                pix = img[row][col]
                img[row][col] = (pix[0],0,0)
        return img

Explanation of code, line by line:

* The above function takes in one input parameter, ``img`` which is the image represented as a 2D list.
* The outer for loop will go through each index of ``img`` which represents the rows of the image.
* The inner for loop will go through each index of ``img[0]``, which represents the columns of the image.
* We assign the tuple ``pix`` to the RGB component, ``img[row][col]``, that we want to access.
* We assign new pixel values as follows: the Red component is set to be the same value as in the original image and the Green and Blue components are set to be zero.
* The function returns the modified image as a 2D list.

Note that this solution will work for any number of rows and columns. It is not locked to a specific size of list.