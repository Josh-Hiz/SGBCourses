import unittest, types
import challenge as task

def defined(name):
    assert name in dir(task), f"Couldn't find a definition for {name}"

def is_fun(name):
    assert isinstance(eval(f"task.{name}"), types.FunctionType), f"Expected {name} to be a function"

class TaskTest(unittest.TestCase):
    def test_defined(self):
        defined('square')
        is_fun('square')
    def test_sample1(self):
        self.assertEqual(task.square([1,2,3,4]),[1,4,9,16])
    def test_sample2(self):
        self.assertEqual(task.square([10,12,15]),[100,144,225])
    def test_empty(self):
        self.assertEqual(task.square([]),[])

unittest.main(exit=False)