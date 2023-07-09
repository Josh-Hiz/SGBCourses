import unittest
import challenge as task

class PxCase(unittest.TestCase):
   def test_sample1(self):
        self.assertEqual(task.create_pixel(255, 0, 0), (255, 0, 0))

   def test_sample2(self):
        self.assertEqual(task.create_pixel(100, 100, 100), (100, 100, 100))

   def test_sample3(self):
        self.assertEqual(task.create_pixel(200, 100, 75), (200, 100, 75))
        
unittest.main(exit=False)