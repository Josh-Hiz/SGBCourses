class Collatz(object):
    def __init__(self, n):
        assert isinstance(n, int), "n must be an int"
        assert n >= 1, "n must be positive"

        self.__n = n
        self.__first = True
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.__first:
            self.__first = False
            return self.__n
        if self.__n == 1: raise StopIteration

        if self.__n % 2 == 0:
            self.__n = self.__n // 2
        else:
            self.__n = 3 * self.__n + 1

        return self.__n