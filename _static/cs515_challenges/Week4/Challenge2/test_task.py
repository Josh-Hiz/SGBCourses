import unittest
from unittest import TestCase
import challenge as task

class AdderCase(TestCase):
    def test_definitions(self):
        self.assertTrue('Adder' in dir(task), 'Adder not defined')
        self.assertTrue('__init__' in dir(task.Adder), '__init__ not present')
        self.assertTrue('add' in dir(task.Adder), 'add not present')

    def test_init(self):
        a = task.Adder(0)
        a = task.Adder(1)
        a = task.Adder(2)

    def test_add(self):
        a = task.Adder(0)
        self.assertEqual(a.add(0), 0, 'Adder(0).add(0)')
        self.assertEqual(a.add(1), 1, 'Adder(0).add(1)')
        b = task.Adder(1)
        self.assertEqual(b.add(0), 1, 'Adder(1).add(0)')
        self.assertEqual(b.add(1), 2, 'Adder(1).add(1)')
        self.assertEqual(a.add(0), 0, 'Adder(0).add(0)')
        self.assertEqual(a.add(1), 1, 'Adder(0).add(1)')
        c = task.Adder(-10)
        self.assertEqual(c.add(0), -10, 'Adder(-10).add(0)')
        self.assertEqual(c.add(1), -9, 'Adder(-10).add(1)')

unittest.main(exit=False)