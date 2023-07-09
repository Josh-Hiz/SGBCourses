from challenge import swap

l = [1,2,3,4]

swap(l, 0, 1)
assert l == [2,1,3,4], "swap 0/1 failed"
swap(l, 1, 0)
assert l == [1,2,3,4], "swap 1/0 failed"

swap(l, 0, -1)
assert l == [4,2,3,1], "swap 0/-1 failed"

swap(l, 0, 0)
assert l == [4,2,3,1], "swap 0/0 failed"

try:
    swap(5, 0, 0)
except AssertionError:
    pass
except:
    assert False, "swap on non-list failed"

try:
    swap(l, 35, -1)
except AssertionError:
    pass
except:
    assert False, "swap 35 (out of bounds)/-1 failed"

try:
    swap(l, 0, 35)
except AssertionError:
    pass
except:
    assert False, "swap 0, 35 (out of bounds) failed"