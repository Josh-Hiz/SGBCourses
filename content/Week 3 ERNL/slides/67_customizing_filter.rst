Customizing red_filter
======================

Previously, you learnt how to define a function to apply the red filter to an entire image as follows:

.. runner::

    # The function takes in one input parameter which is img which is the 
    # image represented as a 2D list.
    def red_filter(img):

        # We provide the entire length of the img which represents the total 
        # number of rows as the range input for the outer for loop. 
        for row in range(len(img)):

            # We provide the length of the first row i.e; img[0] which represents 
            # the total number of columns as the range input for the inner for loop.
            for col in range(len(img[0])):

                # We are accessing the tuple pix which contains the RGB component.
                pix = img[row][col]

                # We are setting assigning new pixel values as follows: the Red 
                # component is set to be the same value as before and the Green and Blue components 
                # are set to be zero.
                img[row][col] = (pix[0],0,0)

        # The function returns the modified image as a 2D list.
        return img

Modifying the above code for Applying red filter to a specified region in an image
----------------------------------------------------------------------------------

Now, let us modify the above function so that the red filter is applied to only the specified region. We will call the new function ``custom_red_filter``. We need to make the following changes to the above function so that it can be customized to a specific region:

* We need the function to take in three more parameters as inputs: ``top_left``, ``height`` and ``width``
* We need to modify the range inputs of the outer for loop to go over only the specified region. The range function's starting point from where we need to iterate would be the row index specified by the top_left tuple which is given by top_left[0] . The iteration should stop once we reach the specified height so the range function's ending point would be top_left[0] + height.
* We need to modify the range inputs of the inner for loop to go over only the specified region. The range function's starting point from where we need to iterate would be the column index specified by the top_left tuple which is given by top_left[1] . The iteration should stop once we reach the specified width so the range function's ending point would be top_left[1] + width.

.. runner::

    def custom_red_filter(img, top_left, height, width):
        for row in range(top_left[0], top_left[0]+height):
            for col in range(top_left[1], top_left[1]+width):
                pix = img[row][col]
                img[row][col] = (pix[0],0,0)
        return img