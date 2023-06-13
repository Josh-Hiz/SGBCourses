import unittest, types
import challenge as task

def defined(name):
    assert name in dir(task), f"Couldn't find a definition for {name}"

def is_fun(name):
    assert isinstance(eval(f"task.{name}"), types.FunctionType), f"Expected {name} to be a function"

class TaskTest(unittest.TestCase):
    def test_defined(self):
        defined('contains_2')
        is_fun('contains_2')
    def test_sample1(self):
        self.assertFalse(task.contains_2([]))
    def test_sample2(self):
        self.assertFalse(task.contains_2([1,3,5,7,9]))
    def test_sample3(self):
        self.assertTrue(task.contains_2([2,6]))
    def test_sample4(self):
        self.assertTrue(task.contains_2([5,3,2,8]))

unittest.main(exit=False)