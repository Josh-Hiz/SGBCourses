def stutter(l):
    '''
    >>> stutter([1,2,3])
    [1, 1, 2, 2, 3, 3]
    >>> stutter([])
    []
    >>> ''.join(stutter(list("soup")))
    'ssoouupp'
    '''
    if len(l) == 0: return []

    return [l[0], l[0]] + stutter(l[1:])