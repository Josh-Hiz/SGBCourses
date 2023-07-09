Flipping with nested for loops
==============================

Let's use nested ``for`` loops to implement *flip*. An initial framework we can think of is as follows:

.. code-block::

    for y in range(len(img)):
        # flip the y-th row

The ``for`` loop lets the variable y take values ``0,1,...,len(img)-1`` one by one, which denotes row indices. The body part is to be filled in so that it flips the y-th row left to right for each iteration. Now, we can just focus on how to flip a single row. Consider the following row of pixels as a fun example.

.. image:: /assets/images/cs515/Week3/flip_rows.png
    :align: center

Here are the steps in details to flip the row image above.

* Swap Pixel 0 and Pixel 6
* Swap Pixel 1 and Pixel 5
* Swap Pixel 2 and Pixel 4

Then, it results in the following image.

.. image:: /assets/images/cs515/Week3/inverse.png
    :align: center

How can this be written in Python? We can interpret the steps above as follows. (Remember we are temporarily at the ``y``-th row now.)

* Swap ``img[y][0]`` and ``img[y][len(img[y]) - 1]``
* Swap ``img[y][1] and img[y][len(img[y]) - 2]`` 

 ⋮

* Swap ``img[y][len(img[y])//2 - 1]`` and ``img[y][len(img[y]) - len(img[y])//2]`` 

However, note that every step can be represented in a generalized form by introducing ``x``, which indicates column indices.

* ``x = 0``: Swap ``img[y][x]`` and ``img[y][len(img) - 1 - x]``
* ``x = 1``: Swap ``img[y][x]`` and ``img[y][len(img) - 1 - x]``

 ⋮

* ``x=len(img[y])//2 - 1``: Swap ``img[y][x]`` and ``img[y][len(img) - 1 - x]``

Notice that the pixels to be swapped are ``img[y][x]`` and ``img[y][len(img) - 1 - x]`` for all steps, regardless of what the value of ``x`` is. Therefore, we can use a for loop with the variable ``x`` taking values in ``range(len(img[y])//2)``. Here is the advanced framework incorporating the ``for`` loop with the variable ``x``.

.. code-block::

    for y in range(len(img)):
        for x in range(len(img[y])//2):
            # Swap img[y][x] and img[y][len(img[y])-x-1]

Now, how do we swap the two pixel values ``img[y][x]`` and ``img[y][len(img[y])-x-1]``? What happens if we just run the following?

.. code-block::

    img[y][x] = img[y][len(img[y])-x-1]
    img[y][len(img[y])-x-1] = img[y][x]

This leads to a wrong outcome because the first line already deletes the original value of ``img[y][x]``, in which case it is impossible to assign the original value of ``img[y][x]`` to ``img[y][len(img[y])-x-1]``. In order to handle this issue, create a temporary variable temp and save the value of ``img[y][x]`` first.

.. code-block::

    temp = img[y][x]

Now that ``temp`` is keeping record of what the original value of ``img[y][x]`` is, we are ready to reassign ``img[y][x]`` to a new value. 

.. code-block::

    img[y][x] = img[y][len(img[y])-x-1]

Then, by assigning ``img[y][len(img[y])-x-1]`` to temp, which denotes the original value of ``img[y][x]``, we complete swapping two pixels.

.. code-block::

    img[y][len(img[y])-x-1] = temp

Here is our final code of nested ``for`` loops that flips ``img`` left to right.

.. code-block::

    for y in range(len(img)):
        for x in range(len(img[y])//2):
            temp = img[y][x]
            img[y][x] = img[y][len(img[y])-x-1]
            img[y][len(img[y])-x-1] = temp