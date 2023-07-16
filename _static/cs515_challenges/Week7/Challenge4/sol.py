def cubes(n):
    assert isinstance(n, int)
    assert n >= 0
    return [i ** 3 for i in range(n+1)]