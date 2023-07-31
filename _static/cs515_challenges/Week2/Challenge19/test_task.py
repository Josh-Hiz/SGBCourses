import unittest, types
from challenge import is_positive_or_multiple_of_7

class TestChallenge(unittest.TestCase):
    
    def test_sample1(self):
        self.assertEqual(is_positive_or_multiple_of_7(100), 91)
    
    def test_sample2(self):
        self.assertEqual(is_positive_or_multiple_of_7(14), 14)
    
    def test_sample3(self):
        self.assertEqual(is_positive_or_multiple_of_7(5), -1)
        
unittest.main(exit=False)