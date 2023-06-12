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
        defined('chain_words')
        is_fun('chain_words')
    def test_sample1(self):
        self.assertEqual(task.chain_words("hello world"), "hello-world")
    def test_sample2(self):
        self.assertEqual(task.chain_words("Connect the words in this sentence"), "Connect-the-words-in-this-sentence")
    def test_empty(self):
        self.assertEqual(task.chain_words(""), "")
    def test_single(self):
        self.assertEqual(task.chain_words("ohhellothere"), "ohhellothere")

unittest.main(exit=False)