def linear_search(v, l):
    '''
    >>> linear_search(0, [0, 1, 2])
    0
    >>> linear_search(0, [1, 0, 2])
    1
    >>> linear_search(0, [2, 1, 0])
    2
    >>> linear_search(0, [3,4,5])
    Traceback (most recent call last):
        ...
    ValueError: not found
    '''
    if len(l) == 0: raise ValueError('not found')

    if l[0] == v: return 0

    return 1 + linear_search(v, l[1:])