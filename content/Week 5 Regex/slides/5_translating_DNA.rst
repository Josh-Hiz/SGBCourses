Translating DNA to amino acids
==============================

Write a function ``translate`` that takes a list of DNA bases and yields a list of amino acids. If there are any bases left over at the end, you should raise an exception (your choice). You should also raise an exception if the string contains something other than DNA bases.

For example:

.. code-block:: 

    >>> translate(list("ATGATCTCGTAA"))
    ['M', 'I', 'S', '_']
    >>> translate([])
    []

Write tests (using doctest or unittest or ``assert``) to check your work. (We won't be 'marking' it---convince yourself you got it right!)

.. challenge:: 

    # define translate, make sure to use some sort of your own testing!