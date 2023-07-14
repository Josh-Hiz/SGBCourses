def nested_concat(v):
    if isinstance(v, str):
        return v
    elif isinstance(v, list):
        if len(v) == 0:
            return ''
        else:
            return nested_concat(v[0]) + nested_concat(v[1:])
    else:
        raise TypeError('nested_sum expects lists (of lists of...) strs')