def sum_and_length(l):
    if len(l) == 0:
        return [0, 0]
    else:
        # you could also write:
        # [s, n] = sum_and_length(l[1:])
        sal = sum_and_length(l[1:])
        s = sal[0]
        n = sal[1]
        return [s+l[0], n+1]