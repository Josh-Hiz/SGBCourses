import unittest, types
import challenge as task

def defined(name):
    assert name in dir(task), f"Couldn't find a definition for {name}"

def is_fun(name):
    assert isinstance(eval(f"task.{name}"), types.FunctionType), f"Expected {name} to be a function"

class TaskTest(unittest.TestCase):
    def test_defined(self):
        defined('factorial')
        is_fun('factorial')
    def test_sample1(self):
        self.assertEqual(task.factorial(0), 1)
    def test_sample2(self):
        self.assertEqual(task.factorial(4), 24)
    def test_empty(self):
        self.assertEqual(task.factorial(5), 120)
    def test_single(self):
        self.assertEqual(task.factorial(1), 1)

unittest.main(exit=False)