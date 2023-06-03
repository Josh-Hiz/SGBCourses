import unittest
import builtins

# set a global default
builtins.fahrenheit = 212

import challenge as temperature

import importlib

class SimpleTestCase(unittest.TestCase):

    def test_defs(self):    
        defs = [v for v in dir(temperature) if v[0] != '_']
        assert 'celsius' in defs, f'Definition for celsius not found'

    def test_212(self):
        builtins.fahrenheit = 212
        importlib.reload(temperature)
        self.assertEqual(temperature.celsius, 100.0)

    def test_32(self):
        builtins.fahrenheit = 32
        importlib.reload(temperature)
        self.assertEqual(temperature.celsius, 0.0)

    def test_bodytemp(self):
        builtins.fahrenheit = 98.6
        importlib.reload(temperature)
        self.assertEqual(temperature.celsius, 37.0)

unittest.main(exit=False)