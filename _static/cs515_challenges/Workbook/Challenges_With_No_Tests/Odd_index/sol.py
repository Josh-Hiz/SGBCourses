def odds(l):
    '''
    >>> odds([])
    []
    >>> odds([1])
    []
    >>> odds([1,2])
    [2]
    >>> str(odds(list("abcdef")))
    "bdf"
    '''
    if len(l) == 0: return []
    if len(l) == 1: return []

    return l[1] + odds(l[2:])