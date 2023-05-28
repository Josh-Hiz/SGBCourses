import unittest
import builtins

# set a global default
builtins.x = 8
builtins.y = 11

import challenge as smaller

import importlib

class SimpleTestCase(unittest.TestCase):

    def test_defs(self):    
        defs = [v for v in dir(smaller) if v[0] != '_']
        assert 'smaller' in defs, f'Definition for smaller not found'

    def correct(self, v_x, v_y):
        builtins.x = v_x
        builtins.y = v_y
        importlib.reload(smaller)
        self.assertEqual(smaller.smaller, min(v_x, v_y))

    def test_sample1(self):
        self.correct(8, 11)

    def test_sample2(self):
        self.correct(12, 5)

    def test_same(self):
        self.correct(0, 0)
        self.correct(1, 1)
        self.correct(-1, -1)

unittest.main(exit=False)