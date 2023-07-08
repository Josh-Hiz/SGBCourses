import unittest
import challenge as task

class SumCase(unittest.TestCase):
    def test_11(self):
        o = task.Sum(1, 1)
        self.assertEqual(o.left, 1, 'left')
        self.assertEqual(o.right, 1, 'right')
        self.assertEqual(o.sum, 2, 'sum')

    def test_12(self):
        o = task.Sum(1, 2)
        self.assertEqual(o.left, 1, 'left')
        self.assertEqual(o.right, 2, 'right')
        self.assertEqual(o.sum, 3, 'sum')

    def test_repr(self):
        self.assertEqual(repr(task.Sum(1, 2)), 'Sum(1, 2)')
        self.assertEqual(repr(task.Sum(50, -3)), 'Sum(50, -3)')

    def test_str(self):
        self.assertEqual(str(task.Sum(1, 2)), '1 + 2 = 3')
        self.assertEqual(str(task.Sum(50, -3)), '50 + -3 = 47')

unittest.main(exit=False)