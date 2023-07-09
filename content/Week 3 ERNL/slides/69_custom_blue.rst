custom_blue_filter
==================

Write the function called ``custom_blue_filter`` that takes in 4 input parameters:

* img - an image represented as a 2D list
* top_left - top left corner of the region where the blue filter needs to be applied
* height - height of the region where the filter needs to be applied
* width - width of the region where the filter needs to be applied

Your function should only modify the ``img`` 2D list; it should return ``None``.

**Blue Filter** - Similar to the red filter explained in this lesson, in a blue filter you need to retain the blue component of the corresponding pixel while making the red and green components to be 0.

**Sample Input 1:**

.. code-block::

    [[(80, 90, 40), (40, 50, 32)], [(23, 44, 56), (67, 231, 23)]]
    (1,1)
    1
    1

**Sample Output 1:**

.. code-block::

    [[(80, 90, 40), (40, 50, 32)], [(23, 44, 56), (0, 0, 23)]]

**Sample Input 2:**

.. code-block::

    [[(80, 90, 40), (40, 50, 32), (231, 111, 110)], [(23, 44, 56), (67, 231, 23), (231, 111, 110)], [(231, 190, 120), (140, 150, 231), (231, 111, 110)]]
    (0,0)
    2
    3

**Sample Output 2:**

.. code-block::

    [[(0, 0, 40), (0, 0, 32), (0, 0, 110)], [(0, 0, 56), (0, 0, 23), (0, 0, 110)], [(231, 190, 120), (140, 150, 231), (231, 111, 110)]]

.. challenge::
    :tester: /_static/cs515_challenges/Week3/Challenge13/test_task.py

    # define custom_blue_filter(img, top_left, height, width)