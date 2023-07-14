def increment_2D(ls):
    res = []
    for l in ls:
        new_l = []

        for x in l:
            new_l.append(x+1)

        res.append(new_l)
    return res