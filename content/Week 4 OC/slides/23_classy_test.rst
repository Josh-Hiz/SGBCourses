Classy testing
==============

We've seen how to test our code with ``doctest``, i.e., by copy/pasting (or just writing from scratch) interactions in the Python REPL and using the ``doctest`` library. Another popular approach is to write tests in a separate file of **unit tests**.

The idea of a unit test is to test a single "unit" of your program. It turns out that ``doctest``'s are a form of unit test, where the unit is a module or definition. The `Python library <https://docs.python.org/3/library/unittest.html>`_ ``unittest`` lets you write similar tests, but in a separate file. In principle, ``doctest`` and ``unittest`` let you do the same things, and both are immensely popular in the Python ecosystem. The ``unittest`` library is a bit heavier duty (i.e, it makes it easier to do some complex things, but it is a bit more verbose). But to our point: the ``unittest`` library works by having you extend a class... so let's get some practice with that!

First, here's some code we'd like to test. There's a bug---but don't worry, we'll find it.

.. runner:: 

    def median(l):
        l = list(l) # copy the list
        l.sort() # sort it
        return l[len(l) // 2] 

To test it with ``unittest``, we define a **test case**. Here's an example of a file that will test the median function.

.. runner:: 

    import unittest

    def median(l):
        l = list(l) # copy the list
        l.sort() # sort it
        return l[len(l) // 2]

    class MedianCase(unittest.TestCase):
        def test_singleton(self):
            self.assertEqual(median([1]), 1)
            self.assertEqual(median([2]), 2)

        def test_int(self):
            self.assertEqual(median([1,2,3]), 2)

        def test_float(self):
            self.assertEqual(median([1.0,2.0,3.0]), 2.0)

Let's piece it all apart. We have an import and our definition. More commonly, we'd import ``median`` from some other module... but Ed doesn't let us do that.

Our test case is defined as a class ``MedianCase``, extending ``unittest.TestCase``. We define several methods that start with ``test_``, which call an internal method to assert some equalities.

To run tests, we run ``python -m unittest -v median.py``, yielding output like:

.. code-block:: 

    $ python -m unittest median.py -v
    test_float (median.MedianCase) ... ok
    test_int (median.MedianCase) ... ok
    test_singleton (median.MedianCase) ... ok

    ----------------------------------------------------------------------
    Ran 3 tests in 0.000s

    OK