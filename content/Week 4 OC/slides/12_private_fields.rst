Private fields with __
======================

Let's reconsider our ``Counter`` class.

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
    c.value = 'hi'
    c.tick()

Oh no! An update to the ``value`` field---outside the class definition itself---caused an exception to be raised inside a class method. That's not good. If you only call the constructor and ``tick``, you'll never have any problems... but if someone else messes with your fields, it could be hard to figure out what's gone wrong.

What we need is **encapsulation**: we need to be able to protect some of the internals of our objects from messed with, so that outside code doesn't mess up our **invariants** (like, e.g., ``Counter.value`` is an ``int``).

Python's approach to encapsulation is a lightweight compromise. Private fields should have names starting with two underscores. Programs should then avoid using those names, which are considered private and internal.

.. runner:: 

    class Counter(object):
        def __init__(self):
            self.__value = 0

        def tick(self):
            self.__value = self.__value + 1

        def value(self):
            return self.__value

    c = Counter()
    c.tick()
    print(c.value())
    c.tick()
    c.tick()
    print(c.value())

    print(c.__value)
    # print(c._Counter__value)

The compromise here is that you can circumvent things. Just naming ``c.__value`` raises an ``AttributeError``. If we instead refer to ``c._Counter__value``, then we can see the internal state. In some languages, you can really and truly make things private. That's hard to do in Python. But it's easy to make things hard to get to in a way that looks weird---which is enough to discourage people from doing it without making it impossible. (Python is a very pragmatic language and is full of compromises like this.)

You'll notice that ``__init__`` has a similar name---it starts with two underscores! The theme here is that things starting with ``__`` aren't for outside consumption.