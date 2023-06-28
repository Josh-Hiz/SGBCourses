Free response question testing
==============================


Free response that does not uses regex to specify answer
--------------------------------------------------------

.. free-r::
    :answer: 6
    :regex: false

    # Question 1

    Suppose use linear search to look for 5 in the list ```[0,1,2,3,4,5,6,7,8,9,10]```. How many comparisons will we perform?


Free response that uses regex to specify answer
-----------------------------------------------

.. free-r::
    :answer: "hello\\n world\\n how are you\?"|'hello\\n world\\n how are you\?'
    :regex: true

    # Question 2

    How would you write the following as a string in Python?

    ```python
    hello
     world
      how are you?
    ```