import unittest
import builtins

# set a global default
builtins.a = 0
builtins.b = 0
builtins.c = 0

import challenge as smallest

import importlib

class SimpleTestCase(unittest.TestCase):

    def test_defs(self):    
        defs = [v for v in dir(smallest) if v[0] != '_']
        assert 'smallest' in defs, f'Definition for smallest not found'

    def correct(self, v_a, v_b, v_c):
        builtins.a = v_a
        builtins.b = v_b
        builtins.c = v_c
        importlib.reload(smallest)
        self.assertEqual(smallest.smallest, min(v_a, v_b, v_c))

    def test_sample1(self):
        self.correct(8, 11, 17)

    def test_others(self):
        self.correct(12, 5, -1)

    def test_same(self):
        self.correct(0, 0, 0)
        self.correct(1, 1, 1)
        self.correct(-1, -1, -1)

unittest.main(exit=False)