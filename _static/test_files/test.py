import unittest

import main as cube

class CubeTest(unittest.TestCase):
    def test_exists(self):
        assert 'cube' in dir(cube), "Couldn't find a definition for 'cube'"
    
    def correct(self, v_n):
        self.assertEqual(cube.cube(v_n), v_n ** 3)

    def test_sample1(self):
        self.correct(8)

    def test_sample2(self):
        self.correct(1)

    def test_sample3(self):
        self.correct(-2)

    def test_sample4(self):
        self.correct(3)

    def test_zero(self):
        self.correct(0)


unittest.main(exit=False)