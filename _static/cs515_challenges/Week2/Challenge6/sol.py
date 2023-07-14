# read a line of words
# print out the sum of the lengths of the words
s = input().split()
print(sum([len(item) for item in s]))