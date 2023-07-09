import unittest
from challenge import red_filter

class TestTask(unittest.TestCase):
    
    def test_sample1(self):
        img = [[(255, 0, 0), (0, 255, 0), (0, 0, 255)], [(255, 0, 0), (0, 255, 0), (0, 0, 255)], [(255, 0, 0), (0, 255, 0), (0, 0, 255)]]
        res = red_filter(img)
        self.assertEqual(res,[[(255, 0, 0), (0, 0, 0), (0, 0, 0)], [(255, 0, 0), (0, 0, 0), (0, 0, 0)], [(255, 0, 0), (0, 0, 0), (0, 0, 0)]])
    
    def test_sample2(self):
        img = [[(1, 2, 3), (4, 5, 6)], [(7, 8, 9), (10, 11, 12)], [(13, 14, 15), (16, 17, 18)], [(19, 20, 21), (22, 23, 24)], [(25, 26, 27), (28, 29, 30)]]
        res = red_filter(img)
        self.assertEqual(res,[[(1, 0, 0), (4, 0, 0)], [(7, 0, 0), (10, 0, 0)], [(13, 0, 0), (16, 0, 0)], [(19, 0, 0), (22, 0, 0)], [(25, 0, 0), (28, 0, 0)]])

unittest.main(exit=False)