def swap(l, i, j):
    if i == j: return

    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp

def find_maximum(l, start):
    assert 0 <= start < len(l)

    max_idx = start
    max_val = l[start]

    for i in range(start+1, len(l)):
        val = l[i]
        if val > max_val:
            max_idx = i
            max_val = val
        i = i + 1
    return max_idx

def selection_sort_desc(l):
    '''
    >>> l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> selection_sort_desc(l)
    >>> l
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    >>> import random; random.shuffle(l); selection_sort_desc(l); l
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    '''
    for i in range(len(l) - 1):
        j = find_maximum(l, i)
        swap(l, i, j)