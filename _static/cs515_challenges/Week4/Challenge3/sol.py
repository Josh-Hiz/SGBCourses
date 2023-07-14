class SmallCounter(object):
    def __init__(self):
        self.__v = 0

    def tick(self):
        self.__v = min(10, self.__v + 1)
    
    def untick(self):
        self.__v = max(0, self.__v - 1)

    def value(self):
        return self.__v