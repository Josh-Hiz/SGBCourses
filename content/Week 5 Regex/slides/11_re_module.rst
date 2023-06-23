The re module
=============

Python has robust support for regular expressions in `the re module <https://docs.python.org/3/library/re.html>`_. There are several useful functions; we'll focus first on ``findall``. Here's an example:

.. runner:: 

    import re

    print(re.findall('be[ea]r', "beer is not good for bears that go to bars"))

And here's its docstring:

**findall** (pattern,string,flags=0)
    
    Return a list of all non-overlapping matches in the string.

    If one or more capturing groups are present in the pattern, return a list of groups; this will be a list of tuples if the pattern has more than one group.

    Empty matches are included in the result.

We'll learn more about capturing groups soon.