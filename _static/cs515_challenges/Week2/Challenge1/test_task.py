import unittest, types
import challenge as task

def defined(name):
    assert name in dir(task), f"Couldn't find a definition for {name}"

def is_fun(name):
    assert isinstance(eval(f"task.{name}"), types.FunctionType), f"Expected {name} to be a function"

class TaskTest(unittest.TestCase):
    def test_defined(self):
        defined('sum_of_ends')
        is_fun('sum_of_ends')
    def correct(self, l):
        if len(l) == 0:
            ans = 0
        else:
            ans = l[0] + l[-1]
        self.assertEqual(task.sum_of_ends(l), ans)
    def test_sample1(self):
        self.correct([8, 11, 12])
    def test_sample2(self):
        self.correct([5])
    def test_sample3(self):
        self.correct([7,8,9,10,11])
    def test_empty(self):
        self.correct([])
    def test_odd(self):
        self.assertEqual(task.sum_of_ends([1,2]), 3)

unittest.main(exit=False)