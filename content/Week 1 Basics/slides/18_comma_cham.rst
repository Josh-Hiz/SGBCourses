Comma Chameleon
===============

In this challenge, your input will be three lines, each containing a string. The first line will be stored in the variable ``s1``, the second in ``s2``, and the third in ``s3``.

Define a variable called ``joined_with_commas`` that holds a string with the contents of ``s1``, followed by a comma, followed by ``s2``, followed by a comma, followed by ``s3``.

**Sample Input 1:**

``s1`` is 'apple'

``s2`` is 'banana'

``s3`` is 'orange'

**Sample Output 1:**

``joined_with_commas`` is apple,banana,orange

**Sample Input 2:**

``s1`` is '1'

``s2`` is '2'

``s3`` is '3'

**Sample Output 2:**

joined_with_commas is 1,2,3

**Sample Input 3:**

``s1`` is 'red'

``s2`` is 'green'

``s3`` is 'blue'

**Sample Output 3:**

``joined_with_commas`` is red,green,blue

.. challenge::
    :tester: /_static/cs515_challenges/Week1/Challenge7/comma_test.py

    # define joined_with_commas
    #   inputs are strings s1, s2, and s3