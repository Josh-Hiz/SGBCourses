import unittest, types
import challenge as task

def defined(name):
    assert name in dir(task), f"Couldn't find a definition for {name}"

def is_fun(name):
    assert isinstance(eval(f"task.{name}"), types.FunctionType), f"Expected {name} to be a function"

class TaskTest(unittest.TestCase):
    def test_defined(self):
        defined('abs_value_list')
        is_fun('abs_value_list')
    def correct(self, l):
        self.assertEqual(list(task.abs_value_list(l)), list(map(abs, l)))
    def test_sample1(self):
        self.correct([1, 0, -3, 5])
    def test_sampel2(self):
        self.correct([-1, -1.5, -2])
    def test_empty(self):
        self.correct([])
    def test_dup(self):
        self.correct([5,5,5,5])
    def test_left(self):
        self.correct([-1, 0, 12])
    def test_right(self):
        self.correct([-1, 0, 13, 56, -15])

unittest.main(exit=False)