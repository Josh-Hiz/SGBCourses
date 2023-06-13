import unittest, types
import challenge as task

def defined(name):
    assert name in dir(task), f"Couldn't find a definition for {name}"

def is_fun(name):
    assert isinstance(eval(f"task.{name}"), types.FunctionType), f"Expected {name} to be a function"

class TaskTest(unittest.TestCase):
    def test_defined(self):
        defined('count_even_odd')
        is_fun('count_even_odd')
    def test_sample1(self):
        self.assertEqual(task.count_even_odd([8,11,3,78,30,2]),[4,2])
    def test_sample2(self):
        self.assertEqual(task.count_even_odd([1,3,5,7,9,11]),[0,6])
    def test_sample3(self):
        self.assertEqual(task.count_even_odd([0,2,4]),[3,0])
    def test_sample4(self):
        self.assertEqual(task.count_even_odd([0,1]),[1,1])
    def test_empty(self):
        self.assertEqual(task.count_even_odd([]),[0,0])

unittest.main(exit=False)