Defining a function for flip
============================

Now that we have flawless code that flips an image, let's create a function so that the transformation can be utilized repeatedly on many images. Define our function as ``flip_left_right`` and let it take ``img`` as its parameter. Then, bring the nested ``for`` loops that we already completed in Step 3 into the body part of the ``flip_left_right`` function as follows.

.. code-block::

    def flip_left_right(img):
        for y in range(len(img)):
            for x in range(len(img[y])//2):
                temp = img[y][x]
                img[y][x] = img[y][len(img[y])-x-1]
                img[y][len(img[y])-x-1] = temp

In order to validate the code, let's use the following example as our test.

.. code-block::

    rgb_square =[[(255,0,0),(0,255,0), (0,0,255)],
                 [(255,0,0),(0,255,0), (0,0,255)],
                 [(255,0,0),(0,255,0), (0,0,255)]]

Note that the first elements of inner lists are all red, the second elements of inner lists are all green, and the third elements of inner lists are all blue. Thus, ``rgb_square`` represents the following image.

.. image:: /assets/images/cs515/Week3/pre_flip.png
    :align: center

In order to use ``rgb_square`` as our test sample to the ``flip_left_right`` function, we run the following lines.

.. code-block::

    flip_left_right(rgb_square)

Then, here is the output, as we wanted!

.. code-block::

    >>> rgb_square
    [[(0, 0, 255), (0, 255, 0), (255, 0, 0)],
    [(0, 0, 255), (0, 255, 0), (255, 0, 0)], 
    [(0, 0, 255), (0, 255, 0), (255, 0, 0)]]

.. image:: /assets/images/cs515/Week3/post_flip.png
    :align: center

Our ``flip_left_right`` function works well for the given test sample ``rgb_square``.

Now, focus on the fact that the ``flip_left_right`` function does not have any ``return`` statement.

.. code-block::

    def flip_left_right(img):
        for y in range(len(img)):
            for x in range(len(img[y])//2):
                temp = img[y][x]
                img[y][x] = img[y][len(img[y])-x-1]
                img[y][len(img[y])-x-1] = temp

It means the ``flip_left_right`` function returns ``None`` no matter what ``img`` is. Then, how does our code work well although the function returns nothing? Recall that a **reference** is a name that refers to the location/address of a value in memory, and that the referred value is called an **object**. When you assign a list to a variable, what it actually does is to assign the variable with a *reference* that points to the list. Passing the argument ``rgb_square`` as parameter img into the ``flip_left_right`` function,

.. code-block::

    flip_left_right(rgb_square)

does not create copies of every pixel value that ``rgb_square`` is associated with, but it rather passes a *reference* to the object. Therefore, the variable ``img`` in the scope of ``flip_left_right`` function is another reference to the same object as ``rgb_square``. Any execution that handles with the reference ``img`` in the scope of ``flip_left_right`` function automatically modifies pixel values of the object, which is why ``rgb_square`` is altered the way we desired.