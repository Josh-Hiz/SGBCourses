Handling edge cases
===================

Now that we have seen how to write the function for applying the red filter to a specific region in an image, let us see how we can handle few edge cases that arise depending on the given input parameters. We will only focus on the following edge cases:

* The given ``height`` is out of bounds which means the given ``height`` parameter when added to the row index given in the ``top_left`` tuple is greater than the total number of rows present in the 2D list.
* The given ``width`` is out of bounds which means the given ``width`` parameter when added to the column index given in the ``top_left`` tuple is greater than the total number of columns present in the 2D list.
* If ``height`` or ``width`` or the elements of the tuple ``top_left`` are negative, it is considered as invalid input.

The way we will handle these cases is returning a message to the user either saying "Input parameter out of bounds" or "Invalid input".

So the function will now be modified as follows:

.. runner::

    def custom_red_filter(img, top_left, height, width):

        # Checking if any of the input parameters are negative
        if top_left[0] < 0  or top_left[1] < 0 or height < 0 or width < 0:
            return "Invalid input"

        # Checking if the height and width are out of bounds
        elif (top_left[0] + height) > len(img) or (top_left[1] + width) > len(img[0]):
            return "Input parameter out of bounds"

        for row in range(top_left[0], top_left[0]+height):
            for col in range(top_left[1], top_left[1]+width):
                pix = img[row][col]
                img[row][col] = (pix[0],0,0)
        return img

Sample 1
--------

.. runner::

    def custom_red_filter(img, top_left, height, width):

        # Checking if any of the input parameters are negative
        if top_left[0] < 0  or top_left[1] < 0 or height < 0 or width < 0:
            return "Invalid input"

        # Checking if the height and width are out of bounds
        elif (top_left[0] + height) > len(img) or (top_left[1] + width) > len(img[0]):
            return "Input parameter out of bounds"

        for row in range(top_left[0], top_left[0]+height):
            for col in range(top_left[1], top_left[1]+width):
                pix = img[row][col]
                img[row][col] = (pix[0],0,0)
        return img

    img = [[(240, 240, 200), (200, 200, 100)],
           [(160, 240, 120), (120, 200, 140)]]

    top_left = (0,1) 
    height = 2 
    width = 2

    print(custom_red_filter(img, top_left, height,width))

Then the output from the function would be:

.. code-block::

    Input parameter out of bounds

This is because ``top_left[1] + width`` would give us 1+2=3 which is greater than the number of columns present in the given 2 Dimensional list.

Sample 2
--------

.. runner::

    def custom_red_filter(img, top_left, height, width):

        # Checking if any of the input parameters are negative
        if top_left[0] < 0  or top_left[1] < 0 or height < 0 or width < 0:
            return "Invalid input"

        # Checking if the height and width are out of bounds
        elif (top_left[0] + height) > len(img) or (top_left[1] + width) > len(img[0]):
            return "Input parameter out of bounds"

        for row in range(top_left[0], top_left[0]+height):
            for col in range(top_left[1], top_left[1]+width):
                pix = img[row][col]
                img[row][col] = (pix[0],0,0)
        return img

    img = [[(240, 240, 200), (200, 200, 100)],
        [(160, 240, 120), (120, 200, 140)]]

    top_left = (0,1) 
    height = -2 
    width = 2

    print(custom_red_filter(img, top_left, height,width))

 Then the output from the function would be:

.. code-block::

    Invalid input

This is because one of the input parameters ``height`` is negative. 

Sample 3
--------

.. runner::

    def custom_red_filter(img, top_left, height, width):

        # Checking if any of the input parameters are negative
        if top_left[0] < 0  or top_left[1] < 0 or height < 0 or width < 0:
            return "Invalid input"

        # Checking if the height and width are out of bounds
        elif (top_left[0] + height) > len(img) or (top_left[1] + width) > len(img[0]):
            return "Input parameter out of bounds"

        for row in range(top_left[0], top_left[0]+height):
            for col in range(top_left[1], top_left[1]+width):
                pix = img[row][col]
                img[row][col] = (pix[0],0,0)
        return img

    img = [[(240, 240, 200), (200, 200, 100)],
        [(160, 240, 120), (120, 200, 140)]]

    top_left = (0,1) 
    height = 3 
    width = 2

    print(custom_red_filter(img, top_left, height,width))

Then the output from the function would be:

.. code-block::

    Input parameter out of bounds

This is because ``top_left[0] + height`` would give us 0+3=3 which is greater than the number of rows present in the given 2D list.