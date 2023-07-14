def swap(l, n, m):
    assert isinstance(l, list)
    assert -len(l) <= n < len(l)
    assert -len(l) <= m < len(l)

    if n == m:
        return

    temp = l[n]
    l[n] = l[m]
    l[m] = temp