# define sum_nested
def sum_nested(d):
    r = 0
    for k,v in d.items():
        if isinstance(d[k],dict):
            r += sum_nested(d[k])
        elif isinstance(d[k], int) or isinstance(d[k], float):
            r+=v
    return r