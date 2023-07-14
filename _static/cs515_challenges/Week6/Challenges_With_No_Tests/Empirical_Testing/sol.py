import random, math

def swap(l, i, j):
    tmp = l[i]
    l[i] = l[j]
    l[j] = tmp

def fisheryates(l):
    # or: for i in range(len(l) - 1, 0, -1):
    i = len(l) - 1
    while i >= 1:
        j = random.randint(0, i) # randint is inclusive
        swap(l, i, j)
        i = i - 1

def broken(l):
    # or: for i in range(len(l) - 1, 0, -1):
    i = len(l) - 1
    while i >= 1:
        j = random.randint(0, len(l) - 1) # 🤪
        swap(l, i, j)
        i = i - 1

def fact(n):
    res = 1
    while n > 1:
        res = res * n
        n = n - 1
    return res

def mean(l):
    return sum(l) / len(l)

def median(l):
    l = list(l)
    l.sort()
    mid = len(l) // 2
    if len(l) % 2 == 0:
        return mean(l[mid-1:mid+1])
    else:
        return(l[mid])

def stddev(l):
    mu = mean(l)

    variance = 0
    for x in l:
        variance = (x - mu) ** 2
    variance = variance / len(l)

    return math.sqrt(variance)

def test_shuffle(f, l):
    print(f'{f.__name__}:')

    h = {}
    for i in range(fact(len(l)) * 1000):
        lshuf = list(l) # copy list
        f(lshuf) # shuffle according to f

        perm = ''.join(lshuf) # permutation as a string
        h[perm] = h.get(perm, 0) + 1

    perms = list(h.keys())
    perms.sort()
    for perm in perms:
        print(f'  {perm}: {h[perm]}')

    vs = h.values()
    print(f'\n  MEAN: {mean(vs)} MEDIAN: {median(vs)} STDDEV: {stddev(vs)}')

test_shuffle(fisheryates, "ABC")
test_shuffle(broken, "ABC")