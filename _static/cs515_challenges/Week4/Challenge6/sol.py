import unittest
from test import median # don't change this line

class MedianCase(unittest.TestCase):
    def test_singleton(self):
        self.assertEqual(median([1]), 1)
        self.assertEqual(median([2]), 2)

    def test_int(self):
        self.assertEqual(median([1,2,3]), 2)

    def test_float(self):
        self.assertEqual(median([1.0,2.0,3.0]), 2.0)

    def test_middle(self):
        self.assertEqual(median([1.0,2.0,3,4]),2.5)

unittest.main(exit=False)