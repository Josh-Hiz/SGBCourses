import unittest, types
import challenge as task

def defined(name):
    assert name in dir(task), f"Couldn't find a definition for {name}"

def is_fun(name):
    assert isinstance(eval(f"task.{name}"), types.FunctionType), f"Expected {name} to be a function"

class TaskTest(unittest.TestCase):
    def test_defined(self):
        defined('compare_strings')
        is_fun('compare_strings')
    def correct(self, first, second):
        self.assertEqual(task.compare_strings(first, second), first == second)
    def test_sample1(self):
        self.correct("red", "blue")
    def test_sample2(self):
        self.correct("red", "red")
    def test_sample3(self):
        self.correct("red", "redder")
    def test_blue(self):
        self.correct("blue", "blue")
    def test_empty(self):
        self.correct("", "")

unittest.main(exit=False)