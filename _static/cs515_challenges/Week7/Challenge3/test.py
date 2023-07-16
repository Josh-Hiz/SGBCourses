import unittest
from challenge import longest_lines

class TestChallenge(unittest.TestCase):
    
    def test_sample_1(self):
        lines = ['a','b','cd','ef','g']
        with open('sample.txt', 'w') as f:
            for line in lines:
                f.write(line + '\n')
            f.close()
        self.assertEqual(longest_lines('sample.txt'), ['cd','ef'])
        
    def test_sample_2(self):
        lines = ['a','b','c','12345','d','e','f']
        with open('sample.txt', 'w') as f:
            for line in lines:
                f.write(line + '\n')
            f.close()
        self.assertEqual(longest_lines('sample.txt'), ['12345'])

unittest.main(exit=False)