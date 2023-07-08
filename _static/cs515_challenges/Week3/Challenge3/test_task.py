import unittest, types
import challenge as task

class TaskTest(unittest.TestCase):
    
    def test_sample1(self):
        self.assertEqual(task.nested_concat(['hello', 'world']),'helloworld')
    def test_sample2(self):
        self.assertEqual(task.nested_concat([]),'')
    def test_empty(self):
        self.assertEqual(task.nested_concat([[[['help'],'i'],['am', 'stuck'],'in'],'a','list']),'helpiamstuckinalist')

unittest.main(exit=False)