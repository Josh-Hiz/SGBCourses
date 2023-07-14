def mapped(f, l):
    if len(l) == 0: return []

    return [f(l[0])] + mapped(f, l[1:])