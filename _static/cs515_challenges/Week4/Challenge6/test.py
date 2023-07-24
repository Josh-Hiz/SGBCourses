def median1(l):
    l = list(l) # copy the list
    l.sort() # sort it
    return l[len(l) // 2]

def median2(l):
    l = list(l) # copy the list
    l.sort() # sort it
    return l[len(l) // 2]

import unittest

class MedianCase(unittest.TestCase):
    def test(self):
        self.assertFalse
        