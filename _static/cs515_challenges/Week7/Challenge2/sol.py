def identity(x): return x

def merge(l1, l2, key=None):
    if key is None:
        key = identity

    if len(l1) == 0: return l2
    if len(l2) == 0: return l1

    if key(l1[0]) < key(l2[0]):
        return [l1[0]] + merge(l1[1:], l2, key=key)
    else:
        return [l2[0]] + merge(l1, l2[1:], key=key)

def mergesort(l, key=None):
    if len(l) < 2: return list(l)

    l1 = mergesort(l[0:len(l) // 2], key=key)
    l2 = mergesort(l[len(l) // 2:], key=key)

    return merge(l1, l2, key=key)

l = [3,1,6,2,9,5,0,4,8,7]
print(mergesort(l))

l = [3,1,6,2,9,5,0,4,8,7,5,4,6,3,7,2,8,1,9,0]
print(mergesort(l))

l = [1,1,3,1,1,1]
print(mergesort(l))

l = [1,1,1,1,1,100]
print(mergesort(l))

l = [{'id': 100, 'name': 'Michael'},
     {'id': 73, 'name': 'Wen-Ding'},
     {'id': 112, 'name': 'Anvay'}]

def get_id(r): return r['id']
def get_name(r): return r['name']

print(mergesort(l, key=get_id))
print(mergesort(l, key=get_name))