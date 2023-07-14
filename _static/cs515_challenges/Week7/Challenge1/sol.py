def minimum(first, second, *rest):
    v = first
    if second < first:
        v = second

    for x in rest:
        if x < v:
            v = x

    return v

def maximum(first, second, *rest):
    v = first
    if second > first:
        v = second

    for x in rest:
        if x > v:
            v = x
    
    return v