import unittest, builtins, importlib

builtins.numstr1 = '0'
builtins.numstr2 = '1'

import challenge as summer

class SimpleTestCase(unittest.TestCase):
    def test_defs(self):    
        defs = [v for v in dir(summer) if v[0] != '_']
        assert 'sum_of_ints' in defs, f'Definition for sum_of_ints not found'

    def correct(self, v_numstr1, v_numstr2):
        builtins.numstr1 = v_numstr1
        builtins.numstr2 = v_numstr2
        importlib.reload(summer)
        self.assertEqual(summer.sum_of_ints, int(v_numstr1) + int(v_numstr2))

    def test_sample1(self):
        self.correct('8', '11')

    def test_sample2(self):
        self.correct('1', '2')

    def test_sample3(self):
        self.correct('100000', '9')

    def test_zeros(self):
        self.correct('0', '0')

    def test_neg(self):
        self.correct('-1', '-1')
        
unittest.main(exit=False)