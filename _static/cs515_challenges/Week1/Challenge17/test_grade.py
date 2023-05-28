import unittest, challenge as grade, types

class TestGrade(unittest.TestCase):
    def test_defined(self):
        defs = [v for v in dir(grade) if v[0] != '_']
        assert 'is_passing' in defs, f'Definition for is_passing not found'
        assert (type(grade.is_passing) == types.FunctionType), 'is_passing must be a function'

    def correct(self, pct):
        self.assertEqual(grade.is_passing(pct), pct >= 60.0)
    def test_sample1(self):
        self.correct(85)
    def test_sample2(self):
        self.correct(25)
    def test_sample3(self):
        self.correct(1500)
    def test_sample4(self):
        self.correct(-300)
    def test_sample5(self):
        self.correct(60)
    def test_sample6(self):
        self.correct(59.99)
    def test_just_barely(self):
        self.correct(60.0001)

unittest.main(exit=False)