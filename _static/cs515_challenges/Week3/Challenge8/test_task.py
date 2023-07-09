import unittest
import challenge as task

class TaskTest(unittest.TestCase):
    
    def test_sample1(self):
        self.assertEqual(task.increment_2D([[1,2],[4,0],[-1]]),[[2, 3], [5, 1], [0]])

unittest.main(exit=False)