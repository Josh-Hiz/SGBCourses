from unittest import TestCase
import unittest
from challenge import SmallCounter

class SCCase(TestCase):
    def test_initial(self):
        self.assertEqual(SmallCounter().value(), 0, 'initial value should be 0')

    def test_private(self):
        c = SmallCounter()
        l = list(filter(lambda s: '__' not in s, dir(c)))
        l.sort()
        expected = ['tick', 'untick', 'value']
        expected.sort()
        self.assertEqual(l, expected, 'only tick, untick, and value should be public')

    def test_tick(self):
        c = SmallCounter()
        c.tick()
        self.assertEqual(c.value(), 1, 'tick should increment')
        c.tick()
        self.assertEqual(c.value(), 2, 'tick should increment again')
        for i in range(100):
            c.tick()
        self.assertEqual(c.value(), 10, 'ticking should stop at 10')
    
    def test_untick(self):
        c = SmallCounter()
        c.untick()
        self.assertEqual(c.value(), 0, 'unticking should decrement but stop at 0')
        c.tick(); c.tick(); c.tick()
        self.assertEqual(c.value(), 3, 'tick should work after untick')
        c.untick()
        self.assertEqual(c.value(), 2, 'untick should work after tick')
        for i in range(100):
            c.tick()
        self.assertEqual(c.value(), 10, 'ticking should stop at 10')
        for i in range(9):
            c.untick()
        self.assertEqual(c.value(), 1, 'unticking should work after saturating at 10')
        c.untick()
        self.assertEqual(c.value(), 0)

    def test_multi(self):
        c1 = SmallCounter()
        c2 = SmallCounter()
        self.assertEqual(c1.value(), 0)
        self.assertEqual(c2.value(), 0)
        c1.tick()
        self.assertEqual(c1.value(), 1)
        self.assertEqual(c2.value(), 0)
        c1.tick()
        self.assertEqual(c1.value(), 2)
        self.assertEqual(c2.value(), 0)
        c2.untick()
        self.assertEqual(c1.value(), 2)
        self.assertEqual(c2.value(), 0)
        for i in range(10):
            c1.tick()
        c2.tick()
        self.assertEqual(c1.value(), 10)
        self.assertEqual(c2.value(), 1)

unittest.main(exit=False)