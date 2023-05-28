import unittest, types, challenge as fun

class FunTest(unittest.TestCase):
    def test_defined(self):
        defs = [v for v in dir(fun) if v[0] != '_']
        assert 'is_less_than_10' in defs, f'Definition for is_less_than_10 not found'
        assert (type(fun.is_less_than_10) == types.FunctionType), 'is_less_than_10 must be a function'

    def correct(self, n):
        self.assertEqual(fun.is_less_than_10(n), n < 10)
    def test_sample1(self):
        self.correct(2)
    def test_sample2(self):
        self.correct(3)
    def test_sample3(self):
        self.correct(11)
    def test_sample4(self):
        self.correct(10)
    def test_zero(self):
        self.correct(0)
    
unittest.main(exit=False)