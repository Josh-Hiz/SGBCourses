import unittest, challenge as shout

class ShoutTest(unittest.TestCase):
    def test_exists(self):
        assert 'exclaim' in dir(shout), "Couldn't find a definition for 'exclaim'"
    def correct(self, s, n):
        self.assertEqual(shout.exclaim(s, n), s + (n * "!"))
    def test_sample1(self):
        self.correct("Hey", 4)
    def test_sample2(self):
        self.correct("Hey", 0)
    def test_sample3(self):
        self.correct("!", 2)
    def test_sample4(self):
        self.correct("Ah", 1)
    def test_empty(self):
        self.correct("", 0)
    def test_empty12(self):
        self.correct("", 12)

unittest.main(exit=False)