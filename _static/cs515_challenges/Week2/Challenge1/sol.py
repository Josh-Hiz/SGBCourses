# define sum_of_ends here
def sum_of_ends(lst):
    if lst == []:
        return 0
    elif len(lst) == 1:
        return lst[0]*2
    else:
        return lst[0] + lst[-1]