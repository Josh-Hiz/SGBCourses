import unittest, types
import challenge as task

def defined(name):
    assert name in dir(task), f"Couldn't find a definition for {name}"

def is_fun(name):
    assert isinstance(eval(f"task.{name}"), types.FunctionType), f"Expected {name} to be a function"

class TaskTest(unittest.TestCase):
    def test_defined(self):
        defined('char_in_string')
        is_fun('char_in_string')
    def correct(self, letter, message):
        self.assertEqual(task.char_in_string(letter, message), letter in message)
    def test_sample1(self):
        self.correct('b', 'book')
    def test_sample2(self):
        self.correct('c', 'book')
    def test_empty(self):
        self.correct("c", "")
    def test_dup(self):
        self.correct("c", "cccc")
    def test_late(self):
        self.correct("c", "bookccc")
