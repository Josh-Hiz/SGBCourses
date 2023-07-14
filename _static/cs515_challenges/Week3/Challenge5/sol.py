def multiplication_tables(num):
    l = []
    for n in range(1,num+1):
        l = []
        for i in range(1,11):
            l.append(n * i)
        print(l)