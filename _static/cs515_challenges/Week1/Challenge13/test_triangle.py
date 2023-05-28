import unittest, challenge as triangle

class TriangleTest(unittest.TestCase):
    def test_exists(self):
        assert 'triangle_area' in dir(triangle), "Couldn't find definition for 'triangle_area'"

    def correct(self, base, height):
        self.assertEqual(triangle.triangle_area(base, height), base * height / 2)

    def test_sample1(self):
        self.correct(5, 6)
    def test_sample2(self):
        self.correct(3, 4)
    def test_sample3(self):
        self.correct(1, 2)
    def test_unit(self):
        self.correct(1, 1)
    def test_half(self):
        self.correct(0.5, 0.5)

unittest.main(exit=False)