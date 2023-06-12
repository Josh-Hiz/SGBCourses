import unittest, types
import challenge as task

def defined(name):
    assert name in dir(task), f"Couldn't find a definition for {name}"

def is_fun(name):
    assert isinstance(eval(f"task.{name}"), types.FunctionType), f"Expected {name} to be a function"

class TaskTest(unittest.TestCase):
    def test_defined(self):
        defined('is_present')
        is_fun('is_present')
    def correct(self, n, l):
        self.assertEqual(task.is_present(n, l), n in l)
    def test_sample1(self):
        self.correct(10, [1,2,3,4,10])
    def test_empty(self):
        self.correct(0, [])
    def test_dup(self):
        self.correct(5, [5,5,5,5])
    def test_late(self):
        self.correct(12, [-1, 0, 12])
    def test_missing(self):
        self.correct(12, [-1, 0, 13])

unittest.main(exit=False)