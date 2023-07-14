def alternate(l1, l2):
    if len(l1) == 0: return list(l2)
    if len(l2) == 0: return list(l1)

    return [l1[0], l2[0]] + alternate(l1[1:], l2[1:])