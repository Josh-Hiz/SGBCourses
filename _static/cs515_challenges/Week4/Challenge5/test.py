import challenge
import unittest

class meanTest(unittest.TestCase):
    
    def mean(self, input_lst):

        def mean1(l):
            return sum(l) / len(l)

        def mean2(l):
            return l[0]

        def mean3(l):
            return l[-1]

        def mean4(l):
            l.sort()
            return float(l[len(l)//2])

unittest.main(exit=False)    