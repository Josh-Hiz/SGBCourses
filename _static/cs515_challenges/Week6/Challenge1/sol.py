import random

def swap(l, i, j):
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp

def fisher_yates(l):
    # or: for i in range(len(l) - 1, 0, -1):
    for i in range(len(l) - 1):
        j = random.randint(i, len(l) - 1) # randint is inclusive
        swap(l, i, j)

l = [1,2,3,4,5,6,7,8,9]
print(l)
for i in range(3):
    fisher_yates(l)
    print(l)