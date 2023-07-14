class Sum(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.sum = left + right
    
    def __repr__(self):
        return f'Sum({self.left}, {self.right})'

    def __str__(self):
        return f'{self.left} + {self.right} = {self.sum}'