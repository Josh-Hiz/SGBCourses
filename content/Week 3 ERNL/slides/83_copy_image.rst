Creating a copy of an image
===========================

We can use nested for loops to help us create copies of 2D lists. The idea is to create an empty list and add each element into this newly created list. Referring to the code below, we want to make a copy of ``img`` which is a 2×22 \times 22×2 image. We first created a new list called ``copy_img`` and used a nested for loop to add each element into this new list. The outer for loop will iterate through the indices of the row. Within this outer for loop, we have created a new empty list called ``row`` which will be used to store the copied values from that particular row in ``img``. Then we have an inner for loop that will iterate through the indices of the column. Within this inner for loop, we append the element at that particular row and column to the ``row`` list. Once this inner for loop finishes, we have successfully copied that particular row in ``img``, ``img[row_idx]``, to ``row``. We then append row to ``copy_img`` and continue to copy the next row until we have finished copying all rows.

.. runner::

    img = [[(0, 0, 0), (255, 255, 255)], [(255, 255, 255), (0, 0, 0)]]
    copy_img = []

    for row_idx in range(len(img)):
        row = []
        for col_idx in range(len(img[row_idx])):
            row.append(img[row_idx][col_idx])
        copy_img.append(row)

    print("img =", img)
    print("copy_img =", copy_img)
    print("id of img =", id(img))
    print("id of copy_img =", id(copy_img))

Our piece of code prints out the following. Notice that ``img`` and ``copy_img`` contain the same elements in the 2D lists. However, they have separate id's, recall from previous modules that separate ids indicate two references that point to separate objects. This means ``img`` and ``copy_img`` contain references that point to separate objects. (The ``id`` numbers printed when you run the code may vary.)

.. code-block::

    img = [[(0, 0, 0), (255, 255, 255)], [(255, 255, 255), (0, 0, 0)]]
    copy_img = [[(0, 0, 0), (255, 255, 255)], [(255, 255, 255), (0, 0, 0)]]
    id of img = 229476360
    id of copy_img = 229755752