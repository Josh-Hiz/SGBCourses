import unittest, types
import challenge as task

def defined(name):
    assert name in dir(task), f"Couldn't find a definition for {name}"

def is_fun(name):
    assert isinstance(eval(f"task.{name}"), types.FunctionType), f"Expected {name} to be a function"

class TaskTest(unittest.TestCase):
    def test_defined(self):
        defined('combined_list_len')
        is_fun('combined_list_len')
    def correct(self, l1, l2):
        self.assertEqual(task.combined_list_len(l1, l2), len(l1) + len(l2))
    def test_sample(self):
        self.correct([10, 13, 25, 57], [2, 455, 238])
    def test_empty(self):
        self.correct([], [])
    def test_dup(self):
        self.correct([5,5,5,5], [5,5,5,5])
    def test_left(self):
        self.correct([-1, 0, 12], [])
    def test_right(self):
        self.correct([], [-1, 0, 13, 56, -15])
    def test_poly(self):
        self.correct(['a','b','c'],[1,2,3])

unittest.main(exit=False)