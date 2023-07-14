# write is_positive_or_multiple_of_7
def is_positive_or_multiple_of_7(n):
    while n % 7 != 0 and n > 0:
        n-=3
    return n