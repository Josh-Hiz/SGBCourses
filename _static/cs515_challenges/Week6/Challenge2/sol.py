# define is_sorted
def is_sorted(l):
    '''
    >>> is_sorted([])
    True
    >>> is_sorted([5])
    True
    >>> is_sorted([0,1,2,3,4])
    True
    >>> is_sorted([0,-1,2,3,4])
    False
    >>> is_sorted([0,1,2,3,0])
    False
    >>> is_sorted([1,2,2,3,3,3])
    True
    >>> is_sorted([-1,2,2,3,3,3])
    True
    >>> is_sorted([-1,2,2,3,3,3,-4])
    False
    '''
    if len(l) < 2: return True

    last = l[0]
    for x in l[1:]:
        if x < last: return False
        last = x
    return True