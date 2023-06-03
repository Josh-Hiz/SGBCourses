import unittest

# Import the student's factorial function from main.py
import challenge as three

class SimpleTestCase(unittest.TestCase):

    def test_defs(self):    
        defs = [v for v in dir(three) if v[0] != '_']
        assert len(defs) == 3, f'Found {len(defs)} definitions, expected 3'

    def test_int(self):
        defs = [v for v in dir(three) if v[0] != '_']
        for d in defs:
            v = eval(f'three.{d}')
            assert type(v) == int or type(v) == float, f'Expected a number for {d}, but got {v}'

unittest.main(exit=False)
        