from challenge import sum_nested
import unittest

class SumCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(sum_nested({}), 0)
    def test_d1(self):
        self.assertEqual(sum_nested({'a': 1, 'b': '2', 'c': 3}), 4)
    def test_d2(self):
        self.assertEqual(sum_nested({'a': 1, 'b': '2', 'c': {'x': 1, 'y': [4, 5], 'z': 2}}), 4)
    def test_deep(self):
        d = {}
        outer = d
        for i in range(50):
            d['a'] = {}
            d = d['a']
        d['b'] = 100

        self.assertEqual(sum_nested(outer), 100)
    def test_deep_empty(self):
        d = {}
        outer = d
        for i in range(50):
            d['a'] = {}
            d = d['a']
        d['b'] = 'alas'

        self.assertEqual(sum_nested(outer), 0)
    def test_deep_list(self):
        d = {}
        outer = {'l': [d], 'boop': 5, 'bedoop': 6 }
        for i in range(50):
            d['a'] = {}
            d = d['a']
        d['b'] = '100'
        
        self.assertEqual(sum_nested(outer), 11)

unittest.main(exit=False)