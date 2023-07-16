Arithmetic overloading
======================

Python allows for some very fancy overloading of just about every operation. We'll briefly show you how to do overloading for numeric operations.

Suppose we want to design a class that lets us work with three-dimensional vectors. There are a number of operations we might want to define:

* vector addition (add the components together)
* scalar addition (add a value to every component)
* scalar multiplication (multiply every component by a value)
* equality (return True on equal vectors)

Python lets us define these operations so that we can use existing Python + and * and == operators. Let's see how. Here's the code:

.. runner::

    import math
    from numbers import Number

    class Vector(object):
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

        def __str__(self): return f'({self.x}, {self.y}, {self.z})'
        def __repr__(self): return f'Vector({self.x}, {self.y}, {self.z})'

        def __add__(self, other):
            print(f'Vector.__add__({self}, {other})')
            if isinstance(other, Vector):
                return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
            
            elif isinstance(other, Number):
                return Vector(self.x + other, self.y + other, self.z + other)

            else:
                return NotImplemented

        def __radd__(self, other):
            print(f'Vector.__radd__({self}, {other})')
            if isinstance(other, Vector):
                return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
            
            elif isinstance(other, Number):
                return Vector(self.x + other, self.y + other, self.z + other)

            else:
                return NotImplemented

        def __mul__(self, other):
            print(f'Vector.__mul__({self}, {other})')

            if isinstance(other, Number):
                return Vector(self.x * other, self.y * other, self.z * other)

            else:
                return NotImplemented
        
        def __rmul__(self, other):
            print(f'Vector.__rmul__({self}, {other})')

            if isinstance(other, Number):
                return Vector(self.x * other, self.y * other, self.z * other)

            else:
                return NotImplemented
        
        def __eq__(self, other):
            print(f'Vector.__eq__({self}, {other})')        
            if isinstance(other, Vector):
                return self.x == other.x and self.y == other.y and self.z == other.z

            return NotImplemented

        def __hash__(self):
            return (self.x, self.y, self.z).hash()

We put some ``print`` statements at overloaded methods to clarify what's getting called when. Here's an example interaction:

We put some ``print`` statements at overloaded methods to clarify what's getting called when. Here's an example interaction:

.. code-block::

    >>> origin = Vector(0, 0, 0)
    >>> v1 = Vector(1, 1, 1)
    >>> x = Vector(1, 0, 0)
    >>> origin + 1
    Vector.__add__((0, 0, 0), 1)
    Vector(1, 1, 1)
    >>> 1 + origin
    Vector.__radd__((0, 0, 0), 1)
    Vector(1, 1, 1)
    >>> origin + 1 == v1
    Vector.__add__((0, 0, 0), 1)
    Vector.__eq__((1, 1, 1), (1, 1, 1))
    True
    >>> origin + v1
    Vector.__add__((0, 0, 0), (1, 1, 1))
    Vector(1, 1, 1)
    >>> v1 + origin
    Vector.__add__((1, 1, 1), (0, 0, 0))
    Vector(1, 1, 1)
    >>> x * 3
    Vector.__mul__((1, 0, 0), 3)
    Vector(3, 0, 0)
    >>> x * 3 + v1
    Vector.__mul__((1, 0, 0), 3)
    Vector.__add__((3, 0, 0), (1, 1, 1))
    Vector(4, 1, 1)

From the sample interactions, we can see that ``__add__`` gets called on the object on the left and ``__radd__`` gets called on the object on the right. But why does the call to ``__radd__`` happen when we write ``1 + origin``? The key is in the ``NotImplemented`` return value.

Overloaded operations tend to take the form of:

* Test ``isinstance`` against the current class, and then return the right answer.
* Test ``isinstance`` against other types that could work, and then return the right answer.
* Give up and return ``NotImplemented`` (or raise ``NotImplementedError``).

Given ``e1 + e2``, Python will first try calling ``e1.__add__(e2)``. If that doesn't work (e.g., ``NotImplemented``), then it will try ``e2.__radd__(e1)``. Since ``int.__add__`` doesn't know about ``Vector``, it gave back a ``NotImplemented``, so ``1 + origin`` called ``origin.__radd__(1)``.

We also overloaded ``__eq__``... and ``__hash__``. Overloading ``__eq__`` lets us define a notion of equality---very convenient! It is *very important* that if you overload ``__eq__``, you overload ``__hash__``. The ``__hash__`` function takes an arbitrary value and produces a number. If two values are ``__eq__`` to each other (i.e., they are equal according to ``==``), then they must have the same hash. Values with the same hash need not be equal, though.

You'll learn more about hashing in a data structures course. For now, it suffices to take any relevant state/members and hash the tuple of them, as our ``__hash__`` here does.