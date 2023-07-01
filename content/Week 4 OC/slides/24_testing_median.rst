Testing median
==============


Complete the tests for the ``median`` function so that the tests *fail*, i.e., write enough tests to help you find the bug.

We'll run your code on the following definition of ``median`` as well as a correct one:

.. code-block:: 

    def median(l):
        l = list(l) # copy the list
        l.sort() # sort it
        return l[len(l) // 2]

.. challenge:: 

    import unittest
    from task import median # don't change this line
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