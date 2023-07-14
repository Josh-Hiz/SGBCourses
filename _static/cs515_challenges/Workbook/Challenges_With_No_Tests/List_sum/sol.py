def sumup(l):
    '''
    >>> sumup([])
    0
    >>> sumup([1])
    1
    >>> sumup([3,1,2])
    6
    >>> sumup([-1,100,1])
    100
    '''
    if len(l) == 0: return 0

    return l[0] + sumup(l[1:])