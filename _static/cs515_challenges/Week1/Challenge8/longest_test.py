import unittest, builtins, importlib

builtins.str1 = "longer"
builtins.str2 = "short"

import challenge as longest

class SimpleTestCase(unittest.TestCase):
    def test_defs(self):    
        defs = [v for v in dir(longest) if v[0] != '_']
        assert 'longer_length' in defs, f'Definition for longer_length not found'

    def correct(self, v_str1, v_str2):
        builtins.str1 = v_str1
        builtins.str2 = v_str2
        importlib.reload(longest)
        self.assertEqual(longest.longer_length, max(len(v_str1), len(v_str2)))

    def test_sample1(self):
        self.correct('longer', 'short')
    
    def test_second(self):
        self.correct('a', 'bc')

    def test_same(self):
        self.correct('', '')
        self.correct('a', 'a')
        self.correct('b', 'a')
        self.correct('a', 'b')
        self.correct('123', '123')
        
unittest.main(exit=False)