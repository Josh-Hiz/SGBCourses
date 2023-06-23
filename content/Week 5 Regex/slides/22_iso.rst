ISO 8601 dates
==============

Write a function ``from8601`` that uses regular expressions to parse an `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_ date. We're interested only in the date part, which can come in one of two formats:

* YYYY-MM-DD
* YYYYMMDD

Your code should return a triple of integers holding the year, month, and day---or raise a ``ValueError`` if things don't work out. Use doctest to check your code! We won't be marking it automatically for you.

.. challenge::

    # define from8601

    