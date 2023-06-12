import unittest, types
import challenge as task

def defined(name):
    assert name in dir(task), f"Couldn't find a definition for {name}"

def is_fun(name):
    assert isinstance(eval(f"task.{name}"), types.FunctionType), f"Expected {name} to be a function"

def is_list(name):
    assert isinstance(eval(f"task.{name}"), list), f"Expected {name} to be a list"

class TaskTest(unittest.TestCase):
    def test_defined(self):
        defined('count_str')
        is_fun('count_str')
    def test_sample1(self):
        self.assertEqual(task.count_str("banana", 'a'), 3)
    def test_sample2(self):
        self.assertEqual(task.count_str("banana", 'n'), 2)
    def test_sample3(self):
        self.assertEqual(task.count_str("a", 'z'), 0)
    def test_count(self):
        self.assertEqual(task.count_str("aaaaa", 'a'), 5)

unittest.main(exit=False)