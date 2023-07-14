def minimum(l):
    '''
    >>> minimum([1])
    1
    >>> minimum([1,-1,0])
    -1
    >>> minimum(list(range(-100,100)))
    -100
    >>> minimum([])
    Traceback (most recent call last):
        ...
    ValueError: empty list has no minimum
    '''
    if len(l) == 0: raise ValueError('empty list has no minimum')

    if len(l) == 1: return l[0]

    first = l[0]
    rest = minimum(l[1:])
    
    if first < rest: return first
    else: return rest
    