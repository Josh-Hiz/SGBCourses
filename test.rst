Free response question testing
==============================

.. free-r::
    :answer: 6

    # Question 1

    Suppose use linear search to look for 5 in the list ```[0,1,2,3,4,5,6,7,8,9,10]```. How many comparisons will we perform?

    ```python
    # Some sample code!
    def linear_search(lst, value):
        for i in range(len(lst)):
            if lst[i] == value:
                return i
        return -1
    ```