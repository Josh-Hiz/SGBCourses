import unittest
import challenge as task

class TaskTest(unittest.TestCase):
    
    def test_sample1(self):
        self.assertEqual(task.sum_and_length([1,2,3]),[6,3])
    def test_sample2(self):
        self.assertEqual(task.sum_and_length([]),[0,0])
    def test_empty(self):
        self.assertEqual(task.sum_and_length([1,2,3,4,5,6,7,8,9,10]),[55,10])

unittest.main(exit=False)