Testing median
==============


Complete the tests for the ``median1`` and ``median2`` function so that the tests *fail*, i.e., write enough tests to help you find the bug between both median functions by writing tests for both that will either pass or fail.

We'll run your code on the following definition of ``median`` (``median2`` in this case) as well as a correct one:

.. code-block:: 

    def median(l):
        l = list(l) # copy the list
        l.sort() # sort it
        return l[len(l) // 2]

.. challenge:: 
    :tester: /_static/cs515_challenges/Week4/Challenge6/test.py

    import unittest
    from test import median1,median2 # don't change this line
    
    class MedianCase(unittest.TestCase):
        def test_singleton(self):
            self.assertEqual(median1([1]), 1)
            self.assertEqual(median1([2]), 2)
            self.assertEqual(median2([1]), 1)
            self.assertEqual(median2([2]), 2)

        def test_int(self):
            self.assertEqual(median1([1,2,3]), 2)
            self.assertEqual(median2([1,2,3]), 2)

        def test_float(self):
            self.assertEqual(median1([1.0,2.0,3.0]), 2.0)
            self.assertEqual(median2([1.0,2.0,3.0]), 2.0)

        # Write more cases below:


    # Dont change this line
    unittest.main(exit=False)