def median1(l):
    l = list(l) # copy the list
    l.sort() # sort it
    return l[len(l) // 2]

def median2(l):
    l = list(l) # copy the list
    l.sort() # sort it
    if len(l) % 2 == 0:
        return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2    
    else:
        return l[len(l) // 2]
        