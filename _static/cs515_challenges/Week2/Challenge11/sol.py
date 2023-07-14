# define fun_with_lists
def fun_with_lists(lst):
    lst.reverse()
    lst.insert(0,'The')
    lst.append('.')
    return lst

print(fun_with_lists(['round', 'is', 'earth']))