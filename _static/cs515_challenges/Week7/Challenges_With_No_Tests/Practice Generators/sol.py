def odds_up_to(n):
    assert isinstance(n, int)
    assert n >= 1

    i = 1
    while i <= n:
        yield i
        i = i + 2

for x in odds_up_to(5): print(x)
for x in odds_up_to(1): print(x)
for x in odds_up_to(2): print(x)