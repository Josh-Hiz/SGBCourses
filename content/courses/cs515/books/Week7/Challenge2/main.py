from algorithms.search import binary_search

l = [9,1,3,7,5,2,4,6,0,8]

l = mergesort(l) # this line will fail until you define algorithms/sort.py and fix the imports

for x in range(0,10):
    assert binary_search(x, l) == x
print("Success: binary search found every element!")