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
        defined('quieter_please')
        is_fun('quieter_please')
    def test_sample1(self):
        self.assertEqual(task.quieter_please("MAKE ME LOWERCASE, PLEASE!"), "make me lowercase, please!")
    def test_sample2(self):
        self.assertEqual(task.quieter_please("i'm already lowercase"), "i'm already lowercase")
    def test_sample3(self):
        self.assertEqual(task.quieter_please("I have both UPPERcase and lowercase"), "I have both UPPERcase and lowercase")
    def test_empty(self):
        self.assertEqual(task.quieter_please(""), "")
    def test_uncased(self):
        self.assertEqual(task.quieter_please("12345"), "12345")
    def test_object_id(self):
        s = "12345abc"
        assert task.quieter_please(s) is s, "The string changed even though it's not uppercase"

unittest.main(exit=False)