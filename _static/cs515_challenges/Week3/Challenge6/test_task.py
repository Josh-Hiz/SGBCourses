import unittest
import challenge as task

class TaskTest(unittest.TestCase):
    
    def test_sample1(self):
        self.assertEqual(task.prime_numbers(10),[2, 3, 5, 7])

unittest.main(exit=False)