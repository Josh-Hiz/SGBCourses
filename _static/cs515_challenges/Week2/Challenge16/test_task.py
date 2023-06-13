import unittest, types
import challenge as task

def defined(name):
    assert name in dir(task), f"Couldn't find a definition for {name}"

def is_fun(name):
    assert isinstance(eval(f"task.{name}"), types.FunctionType), f"Expected {name} to be a function"

class TaskTest(unittest.TestCase):
    def test_defined(self):
        defined('multiply_3')
        is_fun('multiply_3')
    def test_sample1(self):
        self.assertEqual(task.multiply_3(10),270)
    def test_sample2(self):
        self.assertEqual(task.multiply_3(3),243)
    def test_sample3(self):
        self.assertEqual(task.multiply_3(15),135)
    def test_sample4(self):
        self.assertEqual(task.multiply_3(34),102)
    def test_sample5(self):
        self.assertEqual(task.multiply_3(1),243)

unittest.main(exit=False)