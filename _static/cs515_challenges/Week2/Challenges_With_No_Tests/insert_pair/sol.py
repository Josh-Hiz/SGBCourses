# define insert_pair(dictionary, key, value)
def insert_pair(dic,key,val):
    dic[key]=val
    return dic
# we've copied the samples here as tests
# feel free to add your own
assert insert_pair({'instructors': 2, 'TAs': 10, 'tutors': 35, 'students': 600}, 'head tutors', 2) == {'instructors': 2, 'TAs': 10, 'tutors': 35, 'students': 600, 'head tutors': 2}, "sample 1"

assert insert_pair({'CSE': 4, 'MATH': 10}, 'BIO', 4) == {'CSE': 4, 'MATH': 10, 'BIO': 4}

assert insert_pair({}, 10, 2) == {10: 2}