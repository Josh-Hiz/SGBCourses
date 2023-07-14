# define count_even_odd here
def count_even_odd(lst):
    r = [0,0]
    for item in lst:
        if item % 2 == 0:
            r[0]+=1
        else: r[1]+=1
    return r