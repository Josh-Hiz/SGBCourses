def everywhere(f, v):
    '''
    >>> everywhere(lambda n: n + 1, [1, 2, [10, 20, [100]], 1000])
    [2, 3, [11, 21, [101]], 1001]
    '''
    if isinstance(v, list):
        if len(v) == 0: return []

        return [everywhere(f, v[0])] + everywhere(f, v[1:])
    return f(v)