Doctest: putting your tests in your documentation
=================================================

Python has a popular and wonderful approach to testing: put tests into your documentation. The `doctest library <https://docs.python.org/3/library/doctest.html>`_ puts this principle into practice. Here's an example:

.. runner:: 

    def fact(n):
    """Returns factorial of n

    >>> fact(5)
    120
    >>> fact(0)
    1
    >>> fact(-1)
    1
    """
    res = 1
    while n > 1:
        res *= n
        n = n - 1
    return res

The docstring here just has a sample interaction at the Python REPL pasted into it. The ``doctest`` library will find these pasted in interactions, try the code, and warn you if the answer the REPL gives is different from the one you suggest. Here's a log:

.. code-block:: 

    Trying:
        fact(5)
    Expecting:
        120
    ok
    Trying:
        fact(0)
    Expecting:
        1
    ok
    Trying:
        fact(-1)
    Expecting:
        1
    ok
    1 items had no tests:
        fact
    1 items passed all tests:
    3 tests in fact.fact
    3 tests in 2 items.
    3 passed and 0 failed.
    Test passed.

To run this test, you would run ``python -m doctest -v fact.py``. (There are other ways to run the tests, but this is the simplest.)