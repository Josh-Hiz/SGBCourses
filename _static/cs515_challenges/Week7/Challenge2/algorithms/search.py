def linear_search(v, l):
    i = 0
    for x in l:
        if x == v:
            return i
        i = i + 1
    raise ValueError(f'{v} not found')
    
def binary_search(v, l):
    lo = 0
    hi = len(l) - 1
    while lo <= hi:
        mid = lo + ((hi - lo) // 2) # what goes wrong if we use / ?
#        print(f'looking at {mid} between {lo} and {hi}')
        x = l[mid]
        if   v == x: return mid
        elif v <  x: hi = mid - 1
        elif v >  x: lo = mid + 1
    raise ValueError(f'{v} not found')