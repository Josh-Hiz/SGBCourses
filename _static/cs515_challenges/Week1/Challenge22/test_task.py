import unittest
import challenge as task

def defined(name):
    assert name in dir(task), f"Couldn't find a definition for {name}"

class TaskTest(unittest.TestCase):
    def test_defined(self):
        defined('counter')

    def correct(self, expected_count):
        self.assertEqual(task.count, expected_count)
    def test_sample0(self):
        self.correct(0)
    def test_sample1(self):
        task.counter()
        self.correct(1)
    def test_sample2(self):
        task.counter()
        self.correct(2)
    def test_sample3(self):
        task.counter()
        task.counter()
        task.counter()
        self.correct(5)

unittest.main(exit=False)