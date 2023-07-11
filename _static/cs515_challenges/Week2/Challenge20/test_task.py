import unittest, types
import challenge as task

def defined(name):
    assert name in dir(task), f"Couldn't find a definition for {name}"

def is_fun(name):
    assert isinstance(eval(f"task.{name}"), types.FunctionType), f"Expected {name} to be a function"

class TaskTest(unittest.TestCase):
    def test_defined(self):
        defined('find_python')
        is_fun('find_python')
    def test_sample1(self):
        self.assertEqual(task.find_python(['Python','Java','C++']),0)
    def test_sample2(self):
        self.assertEqual(task.find_python('R','Fortran','Python','SQL'),2)
    def test_sample3(self):
        self.assertEqual(task.find_python([]),-1)
    def test_sample4(self):
        self.assertEqual(task.find_python(['Rust','Swift','Kotlin']),-1)

unittest.main(exit=False)