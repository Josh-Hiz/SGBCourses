def prime_numbers(num):
    l = []
    for i in range(2, num+1):
        divisible = False

        for j in range(2, i):
            if i % j == 0:
                divisible = True
                break

        if not divisible:
            l.append(i)

    return l