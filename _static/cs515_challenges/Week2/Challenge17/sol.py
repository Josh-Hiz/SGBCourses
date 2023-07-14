# define abs_more_than_10
#
# use a while loop!
def abs_more_than_10(lst):
    i = 0
    while i < len(lst):
        if abs(lst[i]) > 10: return True
        i+=1
    return False