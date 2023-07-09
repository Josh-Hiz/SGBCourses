Returning an image
==================

Previously, we defined a function for flip that does not have any ``return`` statement. Now, let's consider another form for our function that does have a ``return`` statement. 

.. code-block::

    def flip_left_right(img):
        for y in range(len(img)):
            for x in range(len(img[y])//2):
                temp = img[y][x]
                img[y][x] = img[y][len(img[y])-x-1]
                img[y][len(img[y])-x-1] = temp
        return img

In order to validate the code, let's bring back the same example from Step 7 as our test.

.. code-block::

    rgb_square =[[(255,0,0),(0,255,0), (0,0,255)],
                 [(255,0,0),(0,255,0), (0,0,255)],
                 [(255,0,0),(0,255,0), (0,0,255)]]

.. image:: /assets/images/cs515/Week3/pre_flip.png
    :align: center

In order to use ``rgb_square`` as our test sample to the ``flip_left_right`` function, we run the following lines. Now that our function has a ``return`` statement, we can assign the returned vaule to a new variable ``flipped``.

.. code-block::

    flipped = flip_left_right(rgb_square)

Then, here is the output of ``rgb_square`` and ``flipped``.

.. code-block::

    >>> rgb_square
    [[(0, 0, 255), (0, 255, 0), (255, 0, 0)], 
    [(0, 0, 255), (0, 255, 0), (255, 0, 0)], 
    [(0, 0, 255), (0, 255, 0), (255, 0, 0)]]
    >>> flipped
    [[(0, 0, 255), (0, 255, 0), (255, 0, 0)], 
    [(0, 0, 255), (0, 255, 0), (255, 0, 0)], 
    [(0, 0, 255), (0, 255, 0), (255, 0, 0)]]

.. image:: /assets/images/cs515/Week3/post_flip.png
    :align: center

Thought experiment: how would you change ``flip_left_right`` so that it didn't alter the input ``img`` at all?