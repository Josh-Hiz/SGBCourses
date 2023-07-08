import challenge as task
items = [[1,2,3],[4,5,6],[7,8,9]]
for lst in task.list_2D:
    assert lst in items
    print(lst)