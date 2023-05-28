import unittest
import builtins

# set a global default
builtins.first = -9
builtins.second = 8

import challenge as magnitude

import importlib

class SimpleTestCase(unittest.TestCase):
    def test_defs(self):    
        defs = [v for v in dir(magnitude) if v[0] != '_']
        assert 'larger_magnitude' in defs, f'Definition for larger_magnitude not found'

    def correct(self, v_first, v_second):
        builtins.first = v_first
        builtins.second = v_second
        importlib.reload(magnitude)
        self.assertEqual(magnitude.larger_magnitude, max(abs(v_first), abs(v_second)))

    def test_sample(self):
        self.correct(-9, 8)

    def test_neg(self):
        self.correct(-5, -4)

    def test_pos(self):
        self.correct(4, 5)

    def test_same(self):
        self.correct(0, 0)
        self.correct(1, 1)
        self.correct(-1, -1)

unittest.main(exit=False)