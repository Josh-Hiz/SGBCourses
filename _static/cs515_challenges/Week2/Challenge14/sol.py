# define square
#
# use a for loop, not map!
def square(lst):
    for i in range(len(lst)):
        lst[i] = lst[i]**2
    return lst