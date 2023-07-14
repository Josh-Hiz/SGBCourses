def zip(l1, l2):
    if len(l1) == 0 or len(l2) == 0: return []

    return [(l1[0], l2[0])] + zip(l1[1:], l2[1:])