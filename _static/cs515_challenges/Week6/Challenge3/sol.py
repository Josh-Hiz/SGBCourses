def insert_sorted(v, l):
    if len(l) == 0: return [v]

    i = 0
    res = []
    while i < len(l):
        x = l[i]
        if v < x: return res + [v] + l[i:]

        res.append(x)
        i = i + 1


def insertion_sort(l):
    '''
    >>> insertion_sort([10,0,8,5,3,9,2,7,1,4,6])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    '''
    res = []
    for x in l:
        res = insert_sorted(x, res)
    return res
