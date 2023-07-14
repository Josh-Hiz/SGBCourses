# read several space-separated integers, sum them, then output the sum
s = input().split()
sList = list(map(lambda x: int(x), s))
print(sum(sList))