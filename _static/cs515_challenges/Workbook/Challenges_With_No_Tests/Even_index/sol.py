def evens(l):
    '''
    >>> evens(['a', 'b', 'c', 'd'])
    ['a', 'c']
    >>> evens(['a', 'b', 'c', 'd', 'e'])
    ['a', 'c', 'e']
    >>> evens(['a', 'b'])
    ['a']
    >>> evens([1])
    [1]
    >>> evens([])
    []
    '''
    if len(l) == 0: return []
    if len(l) == 1: return list(l)

    return [l[0]] + evens(l[2:])