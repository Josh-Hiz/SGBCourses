def merge(l1, l2):
    res = []
    i1 = 0
    i2 = 0
    while i1 < len(l1) and i2 < len(l2):
        if l1[i1] < l2[i2]:
            elt = l1[i1]
            i1 = i1 + 1
        else:
            elt = l2[i2]
            i2 = i2 + 1
        res.append(elt)

    if i1 == len(l1):
        res.extend(l2[i2:])
    else:
        res.extend(l1[i1:])

    return res

def split(l):
    left = []
    right = []

    go_left = False
    for x in l:
        if go_left:
            left.append(x)
        else:
            right.append(x)

        go_left = not go_left

    return (left, right)

def mergesort(l):
    '''
    >>> mergesort([3,1,6,2,9,5,0,4,8,7])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> mergesort([3,1,6,2,9,5,0,4,8,7,5,4,6,3,7,2,8,1,9,0])
    [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
    >>> mergesort([1,1,3,1,1,1])
    [1, 1, 1, 1, 1, 3]
    >>> mergesort([1,1,1,1,1,100])
    [1, 1, 1, 1, 1, 100]
    '''
    if len(l) < 2: return list(l)

    ls = split(l)

    l1 = mergesort(ls[0])
    l2 = mergesort(ls[1])

    return merge(l1, l2)

