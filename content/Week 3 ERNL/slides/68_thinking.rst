Thinking about custom_red_filter
================================

Now that we have defined the function for the custom red filter as below, let us analyze its execution on few inputs:

.. runner::


    def custom_red_filter(img, top_left, height, width):
        for row in range(top_left[0], top_left[0]+height):
            for col in range(top_left[1], top_left[1]+width):
                pix = img[row][col]
                img[row][col] = (pix[0],0,0)
        return img

    img = [[(240, 240, 200), (200, 200, 100)],
           [(160, 240, 120), (120, 200, 140)]]

    top_left = (0,1) 
    height = 2 
    width = 1

    print(custom_red_filter(img, top_left, height, width))

The output, lightly formatted, is:

.. code-block::

    [[(240, 240, 200), (200, 0, 0)], 
     [(160, 240, 120), (120, 0, 0)]]

Let us analyze how we arrive at this output when we call the function ``custom_red_filter`` with the above given inputs.

* The outer for loop goes from ``top_left[0]`` which is 0 to ``top_left[0] + height`` which is 0+2 = 2. So the outer for loop range would be 0 to 2 (not inclusive). This means that the outer for loop runs for two iterations covering two rows: row index 0 and row index 1 (since range starts from 0 and goes till 2 which is the end point and the end point specified in range function is not inclusive.
* The inner for loop goes from ``top_left[1]`` which is 1 to ``top_left[1] + width`` which is 1+1 = 2. So the inner for loop range would be 1 to 2 (not inclusive). This means that the inner for loop runs for one iteration covering one column: column index 1 (since range starts from 1 and goes till 2 which is the end point and the end point specified in range function is not inclusive)

So we can see in the final output that the pixel at **(row index 0, column index 1)** and pixel at **(row index 1, column index 1)** is only modified to have the blue and green components to be 0 while retaining the red component.

Similarly, try to analyze how we arrived at the output for the 4*4 image specified when we introduced ``red_filter`` of this lesson.