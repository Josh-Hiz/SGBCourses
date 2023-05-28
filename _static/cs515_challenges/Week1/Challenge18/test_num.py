import unittest, challenge as num, types

class TestNum(unittest.TestCase):
    def test_defined(self):
        defs = [v for v in dir(num) if v[0] != '_']
        assert 'get_num_type' in defs, f'Definition for get_num_type not found'
        assert (type(num.get_num_type) == types.FunctionType), 'get_num_type must be a function'

    def correct(self, n):
        if n == 0:
            descr = "zero"
        else:
            if n < 0:
                sign = "negative"
            else:
                sign = "positive"
            
            if n % 2 == 0:
                parity = "even"
            else:
                parity = "odd"
            
            descr = f'{sign} and {parity}'
        self.assertEqual(num.get_num_type(n), descr)
    def test_sample(self):
        self.correct(11)
    def test_zero(self):
        self.correct(0)
    def test_poseven(self):
        self.correct(12)
    def test_negodd(self):
        self.correct(-1)
    def test_negeven(self):
        self.correct(-5000)
    
unittest.main(exit=False)