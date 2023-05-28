import unittest, types
import challenge as task

def defined(name):
    assert name in dir(task), f"Couldn't find a definition for {name}"

def is_fun(name):
    assert isinstance(eval(f"task.{name}"), types.FunctionType), f"Expected {name} to be a function"

class TaskTest(unittest.TestCase):
    def test_defined(self):
        defined('get_name_length')
        is_fun('get_name_length')
    def correct(self, first, last):
        self.assertEqual(task.get_name_length(first, last), len(first) + len(last))
    def test_sample1(self):
        self.correct("Winnie", "Wilson")
    def test_sample2(self):
        self.correct("Annie", "Wai")
    def test_sample3(self):
        self.correct("Adalbert Gerald", "Soosai Raj")
    def test_empty(self):
        self.correct("", "")
        
unittest.main(exit=False)