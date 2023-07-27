Testing mean
============

Suppose you're writing a function that computes the arithmetic mean (i.e., average, i.e., sum and divide by the length) of a list of numbers. You'd like to test your function. Which examples should you run?

Here is a sample you can run on **IDLE**:

.. code-block:: 

    >>> from example import mean

    Please don't edit the line above---we need it for the code to work. Write as many doctests as you like for the function `mean` below.

    Here's one to start you off:

    >>> mean([1])
    1.0

Consider using the following definitions of ``mean``:

.. code-block::

    # Definition of mean that only returns the first element
    def mean(l):
        return l[0]

    # Definition of mean that only returns the last element
    def mean(l):
        return l[-1]

    # The correct definition
    def mean(l):
        return sum(l) / len(l)

    # Returns the median instead of the mean
    def mean(l):
        l.sort()
        return float(l[len(l)//2])

Here are a few function calls you can use to test your function:

.. code-block::

    >>> mean([1,2,3])
    2.0
    >>> mean([3,1,2])
    2.0
    >>> mean([2,1])
    1.5
    >>> mean([1,2])
    1.5

These tests ensure that the following events do not happen:

* The function does not return the first element of the list
* The function does not return the last element of the list
* The function does not return the median of the list

It is important that all possible cases are concidered when making a function!