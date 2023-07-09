red_filter, in place
====================

Define ``red_filter`` function that takes a 2D list ``img`` as its parameter. The function has to maintain the R components of ``img`` but reduce its G, B components all as 0. Define the function without any ``return`` statement, i.e., it should mutate ``img`` in place.

**Sample Input 1:**

.. code-block::

    [[(255, 0, 0), (0, 255, 0), (0, 0, 255)], [(255, 0, 0), (0, 255, 0), (0, 0, 255)], [(255, 0, 0), (0, 255, 0), (0, 0, 255)]]

**Sample Output 1:**

.. code-block::

    [[(255, 0, 0), (0, 0, 0), (0, 0, 0)], [(255, 0, 0), (0, 0, 0), (0, 0, 0)], [(255, 0, 0), (0, 0, 0), (0, 0, 0)]]

**Sample Input 2:**

.. code-block::

    [[(1, 2, 3), (4, 5, 6)], [(7, 8, 9), (10, 11, 12)], [(13, 14, 15), (16, 17, 18)], [(19, 20, 21), (22, 23, 24)], [(25, 26, 27), (28, 29, 30)]]
    
**Sample Output 2:**

.. code-block::

    [[(1, 0, 0), (4, 0, 0)], [(7, 0, 0), (10, 0, 0)], [(13, 0, 0), (16, 0, 0)], [(19, 0, 0), (22, 0, 0)], [(25, 0, 0), (28, 0, 0)]]

.. challenge::
    :tester: /_static/cs515_challenges/Week3/Challenge16/test.py

    # define red_filter(img)
    # be sure to mutate img in place