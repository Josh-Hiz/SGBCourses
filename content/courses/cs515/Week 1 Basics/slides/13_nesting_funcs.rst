Nesting Function Calls
======================

Just like we can nest arithmetic expressions and use variable names with operators, like in (1 + 2) * 4 or (number_of_tas * 2) we can also use expressions and variables as arguments to functions. In addition, their results can be stored in variables. For example, we could write:

.. code-block:: python

        >>> x = 10
        >>> y = 17
        >>> max(x, y)
        17
        >>> z = max(x, y)
        >>> z + 4
        21

A few more examples:

.. code-block:: python

        >>> min(max(1, 2), 3)
        2
        >>> x = 10
        >>> y = -17
        >>> max(abs(x), abs(y))
        17


.. quizdown::

    ## Which of the programs below end in valid functuion calls? Try them out if you're not sure!

    - [x] ```max(abs(1) 2)```
    - [ ] ```min(max(1,2), 300)```
    - [ ] ```x=100```<br>```abs(max(x,10))```
    - [x] ```max(max(4,5),6)```
    - [ ] ```abs(abs(max(4,5))```
    - [ ] ```x = abs(-3)<br>max(x,x+1)```