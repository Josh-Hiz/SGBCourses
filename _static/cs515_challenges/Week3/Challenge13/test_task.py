from challenge import custom_blue_filter
import unittest, sys
from io import StringIO

class TestChallenge(unittest.TestCase):

    def test_sample1(self):
        img = [[(80, 90, 40), (40, 50, 32)], [(23, 44, 56), (67, 231, 23)]]
        res = custom_blue_filter(img, (1,1), 1, 1)
        assert res is None, "you must return None"
        self.assertEqual(img,[[(80, 90, 40), (40, 50, 32)], [(23, 44, 56), (0, 0, 23)]] )
    
    def test_sample2(self):
        img = [[(80, 90, 40), (40, 50, 32), (231, 111, 110)], [(23, 44, 56), (67, 231, 23), (231, 111, 110)], [(231, 190, 120), (140, 150, 231), (231, 111, 110)]]
        res = custom_blue_filter(img, (0,0), 2, 3)
        assert res is None, "you must return None"
        self.assertEqual(img,[[(0, 0, 40), (0, 0, 32), (0, 0, 110)], [(0, 0, 56), (0, 0, 23), (0, 0, 110)], [(231, 190, 120), (140, 150, 231), (231, 111, 110)]] )

unittest.main(exit=False)

