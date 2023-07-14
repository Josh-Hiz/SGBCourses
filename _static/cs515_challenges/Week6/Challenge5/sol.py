def swap(l, i, j):
    if i == j: return

    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp

def partition(l, pivot, lo, hi):
#    print(f'partition({l[lo:hi+1]}, {pivot}, {lo}, {hi})')

    while True:
        while l[lo] < pivot:
            lo = lo + 1

        while l[hi] > pivot:
            hi = hi - 1

        if lo >= hi: return hi

        swap(l, lo, hi)

        # make sure the next round skips past these swapped values
        lo = lo + 1
        hi = hi - 1

def quicksort_range(l, lo, hi):
    if lo < 0 or hi < 0 or lo >= hi: return
#    print(f'quicksort({l[lo:hi+1]}, {lo}, {hi})')
    mid = lo + ((hi - lo) // 2)

    if l[lo] < l[mid]:
        pivot = min(l[mid], l[hi])
    else:
        pivot = min(l[lo], l[hi])
    p = partition(l, pivot, lo, hi)
    quicksort_range(l, lo, p)
    quicksort_range(l, p+1, hi)

def quicksort(l):
    '''
    >>> l = [3,1,6,2,9,5,0,4,8,7]
    >>> quicksort(l); l
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> l = [3,1,6,2,9,5,0,4,8,7,5,4,6,3,7,2,8,1,9,0]; quicksort(l); l
    [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
    >>> l = [1,1,3,1,1,1]; quicksort(l); l
    [1, 1, 1, 1, 1, 3]
    >>> l = [1,1,1,1,1,100]; quicksort(l); l
    [1, 1, 1, 1, 1, 100]
    '''
    quicksort_range(l, 0, len(l) - 1)

