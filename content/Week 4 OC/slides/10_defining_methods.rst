Defining methods
================

So far, we've defined fields, but the only method we've defined is the specially named ``__init__`` constructor. Let's do some more interesting work!

To define a method, you add ``def NAME(self, ARGS, ...)`` to the class definition block, like so:

.. runner:: 

    class Counter(object):
        def __init__(self):
            self.value = 0

        def tick(self):
            self.value = self.value + 1

    c = Counter()
    print(c.value)
    c.tick()
    print(c.value)
    c.tick()
    c.tick()
    print(c.value)

    # each counter has its own state
    c2 = Counter()
    print(c2.value)
    print(c.value)

Ah: a simple counter! You can define as many methods as you like. Here, we define a version with a ``reset`` method that sets the value back to 0:

.. runner:: 

    class Counter(object):
        def __init__(self):
            self.value = 0

        def tick(self):
            self.value = self.value + 1

        def reset(self):
            self.value = 0

    c = Counter()
    print(c.value)
    c.tick()
    print(c.value)
    c.tick()
    c.tick()
    print(c.value)

    c.reset()
    print(c.value)

The order in which you define methods doesn't matter at all---they all just go in the class definition block.

Method arguments
----------------

Methods take arguments, just like functions. Here's a counter that lets you increment by some amount:

.. runner:: 

    class Counter(object):
        def __init__(self):
            self.value = 0

        def tick(self, inc):
            self.value = self.value + inc

        def reset(self):
            self.value = 0

    c = Counter()
    c.tick(1)
    c.tick(2)
    print(c.value)