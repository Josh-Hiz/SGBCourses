import unittest
import builtins

# set a global default
builtins.s1 = 'apple'
builtins.s2 = 'banana'
builtins.s3 = 'orange'

import challenge as comma

import importlib

class SimpleTestCase(unittest.TestCase):
    def test_defs(self):    
        defs = [v for v in dir(comma) if v[0] != '_']
        assert 'joined_with_commas' in defs, f'Definition for joined_with_commas not found'

    def correct(self, v_s1, v_s2, v_s3):
        builtins.s1 = v_s1
        builtins.s2 = v_s2
        builtins.s3 = v_s3
        importlib.reload(comma)
        self.assertEqual(comma.joined_with_commas, v_s1 + ',' + v_s2 + ',' + v_s3)

    def test_sample1(self):
        self.correct('apple', 'banana', 'orange')

    def test_sample2(self):
        self.correct('1', '2', '3')

    def test_sample3(self):
        self.correct('red', 'green', 'blue')

    def test_commas(self):
        self.correct(',', ',', ',')
        
unittest.main(exit=False)