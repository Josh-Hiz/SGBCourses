Tuples
======

Now you may be wondering how we can represent the RGB model in Python. We can represent a color with a new type of data called a tuple. A **tuple** is an immutable collection of objects: immutable meaning that it cannot be modified once it is created. You can imagine tuples to be like immutable lists. In Python, a tuple is represented similarly to a list except with **round brackets** or **parenthesis** ``()`` rather than square brackets ``[]``.

Below is a tuple of 3 integers, 255, 0, and 0. 

.. code-block::

    red = (255,0,0)

Similar to lists, we can access values in a tuple from **indexing**. To get the first value in red, we can index the 0th index which will print out 255. Note that indexing here is the same as lists with the square brackets ``[]``.

.. runner::

    red = (255,0,0)
    print(red[0])