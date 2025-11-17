Working with fields
===================

To use a field, you can simply refer to it on an object. Here's an example where we add a field to an instance of our ``Empty`` class:

.. runner:: 

    class Empty(object):
        pass

    e = Empty()
    e.a = 'howdy'
    print(e.a)

Notice that we've only set the ``a`` field on the object ``e``, and instance of ``Empty``. Other instances don't have it. Edit the code above to explore that idea!

Notice that we've only set the ``a`` field on the object ``e``, and instance of ``Empty``. Other instances don't have it. Edit the code above to explore that idea! If you try to access an uninitialized field, you'll get an ``AttributeError``:

.. runner:: 

    class Empty(object):
        pass

    e = Empty()
    print(e.a)

A common and useful idiom is to set fields on an object in the constructor. Here's an example of a class that acts a bit like a 2-tuple: it holds two things.

.. runner:: 

    class Pair(object):
        def __init__(self, one, two):
            self.thing1 = one
            self.thing2 = two

    p = Pair('hi', 5)
    print(p.thing1)
    print(p.thing2)

    p.thing1 = 'Johnny'
    print(p.thing1)
    print(p.thing2)

    p.thing2 = '$'
    print(p.thing1)
    print(p.thing2)

A confusing, but common idiom is to use the same name for arguments to a constructor and the field they'll be setting, as in:

.. runner:: 

    class Pair(object):
        def __init__(self, thing1, thing2):
            self.thing1 = thing1
            self.thing2 = thing2

    p = Pair('hi', 5)
    print(p.thing1)
    print(p.thing2)