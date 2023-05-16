# copy in mergesort here, then run the test file

l = [{'id': 100, 'name': 'Michael'},
     {'id': 73, 'name': 'Wen-Ding'},
     {'id': 112, 'name': 'Anvay'}]

def get_id(r): return r['id']
def get_name(r): return r['name']

print(mergesort(l, key=get_id))
print(mergesort(l, key=get_name))