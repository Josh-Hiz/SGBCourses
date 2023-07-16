import math
from numbers import Number

class Coord(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self): return f'({self.x}, {self.y})'
    def __repr__(self): return f'Coord({self.x}, {self.y})'

    def __add__(self, other):
        if isinstance(other, Coord):
            return Coord(self.x + other.x, self.y + other.y)
        
        elif isinstance(other, Number):
            return Coord(self.x + other, self.y + other)

        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Coord):
            return Coord(self.x + other.x, self.y + other.y)
        
        elif isinstance(other, Number):
            return Coord(self.x + other, self.y + other)

        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Number):
            return Coord(self.x * other, self.y * other)

        else:
            return NotImplemented
    
    def __rmul__(self, other):
        if isinstance(other, Number):
            return Coord(self.x * other, self.y * other)

        else:
            return NotImplemented
    

    def __eq__(self, other):
        if isinstance(other, Coord):
            return self.x == other.x and self.y == other.y

        return NotImplemented

    def __hash__(self):
        return (self.x, self.y).hash()
