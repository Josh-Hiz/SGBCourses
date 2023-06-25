Quicksort with median pivot
===========================

The ideal choice for the pivot is the median value: it will generate balanced halves. There are algorithms for quickly finding the approximate median of a list, with varying levels of precision. We'll implement a very simple approach that happens to perform well in practice: calculate the median of the first, middle, and last elements of the range being considered.

Copy over the quicksort code and alter it to use this pivot calculation scheme. The 'Mark" button just runs doctest.

.. challenge:: 
    :tester: /_static/cs515_challenges/Week6/Challenge5/doc.py

    # copy over quicksort
    # use the median of first/middle/last pivot scheme
