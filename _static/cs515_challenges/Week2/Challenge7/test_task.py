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
        for x in [1, 2, 3]:
            l = f'list{x}'
            defined(l)
            is_list(l)
            assert eval(f'task.{l}') == [5,6,7,8,9,10], f'{l} has the wrong value'
    def test_list2_list3_same(self):
        assert id(task.list2) == id(task.list3), 'Expected list2 and list3 to be the same object, but they are different'
    def test_list1_different(self):
        assert id(task.list1) != id(task.list2), 'Expected list1 and list2 to be different objects, but they are the same'
        assert id(task.list1) != id(task.list3), 'Expected list1 and list3 to be different objects, but they are the same'

unittest.main(exit=False)