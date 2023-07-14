# define find_python
def find_python(lst):
    index = -1
    for i in range(len(lst)):
        if lst[i] == 'Python':
            index = i
            break
    return index
    