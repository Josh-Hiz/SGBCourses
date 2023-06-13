import unittest, types
import challenge as task
import ast
import inspect

def defined(name):
    assert name in dir(task), f"Couldn't find a definition for {name}"

def is_fun(name):
    assert isinstance(eval(f"task.{name}"), types.FunctionType), f"Expected {name} to be a function"

def has_while_loop(function):
    source_code = inspect.getsource(function)
    parsed_ast = ast.parse(source_code)

    for node in ast.walk(parsed_ast):
        if isinstance(node, ast.While):
            return True
    return False

class TaskTest(unittest.TestCase):
    def test_defined(self):
        defined('abs_more_than_10')
        is_fun('abs_more_than_10')
    def test_sample1(self):
        self.assertTrue(task.abs_more_than_10([8,-4,7,12]))
    def test_sample2(self):
        self.assertTrue(task.abs_more_than_10([-17,3,4]))
    def test_sample3(self):
        self.assertTrue(task.abs_more_than_10([13,0]))
    def test_sample4(self):
        self.assertFalse(task.abs_more_than_10([-10,2,-5]))
    def test_sample5(self):
        self.assertFalse(task.abs_more_than_10([]))
    def test_sample6(self):
        self.assertTrue(task.abs_more_than_10([0,1,99,99,-99]))
    def test_sample7(self):
        self.assertFalse(task.abs_more_than_10([-9,2,-5,0,2,5,-9,0,0,9]))
    def test_sample8(self):
        self.assertTrue(has_while_loop(task.abs_more_than_10))

unittest.main(exit=False)