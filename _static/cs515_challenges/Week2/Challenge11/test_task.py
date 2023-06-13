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
        defined('fun_with_lists')
        is_fun('fun_with_lists')
    def test_sample1(self):
        self.assertEqual(task.fun_with_lists(['round', 'is', 'earth']), ['The', 'earth', 'is', 'round', '.'])
    def test_sample2(self):
        self.assertEqual(task.fun_with_lists(['program', 'world', 'hello']), ['The', 'hello', 'world', 'program', '.'])
    def test_empty(self):
        self.assertEqual(task.fun_with_lists([]), ['The', '.'])
    def test_single(self):
        self.assertEqual(task.fun_with_lists(['The']), ['The', 'The', '.'])

unittest.main(exit=False)