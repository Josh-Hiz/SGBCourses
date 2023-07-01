Defining objects: classes
=========================

Defining a class in Python involves giving a class name and a base class. By default, we'll use ``object`` as our base class---it's the default choice.

Here's a completely empty class. The ``pass`` keyword does nothing; we need it because you can't have an empty declaration.

.. runner::

    class Empty(object):
        pass

    e = Empty()
    print(f'{e} has id {id(e)}')
    e2 = Empty()
    print(f'{e2} has id {id(e2)}')

The format for the class header is: ``class NAME(BASE)``, where ``NAME`` is the name of the class we're defining and ``BASE`` is the name of the base class. For now ``BASE`` should always be ``object``, and ``NAME`` should always be written in ``CamelCase``, i.e., each word's first letter is capitalized, but the rest is lowercase.

The body of a class is always indented a level in---notice that ``pass`` is indented.

By default, ``Empty`` will have a constructor that does nothing. We can create new instances of Empty, and we can observe that the constructor returns a new object each time. But... that's about it. To make things more interesting, we should define a constructor. To do so, we define a method called ``__init__``.

.. runner:: 

    class Greeter(object):
        def __init__(self):
            print(f"I'm being constructed! My id is {id(self)}.")

    g = Greeter()
    print(id(g))
    g2 = Greeter()
    print(id(g2))

There's quite a bit to unpack here. To define the ``__init__`` method, we indented a level and used ``def``, just like if we were defining a function. But ``__init__`` also takes an argument, ``self``. Which is pretty weird, considering that the call to the constructor doesn't take *any* arguments!

The key to object-oriented programming is understanding self-reference, here using the ``self`` keyword. (Other languages use ``this``, among other things.) **Every method in a class takes an extra argument, self**. Since every method can see ``self``, it means that the code and data are grouped together.

Here we don't have any data stored in ``self`` yet, but we *can* observe that the ``self`` inside the constructor is the same thing that the constructor returns. Here's a run (you may get different ``id``'s):

.. code-block:: 

    I'm being constructed! My id is 140598014959136.
    140598014959136
    I'm being constructed! My id is 140598014957360.
    140598014957360

Notice that the ``id`` printed out inside of the method is the same as the one immediately returned.

``__init__`` is a weird name
----------------------------

In Python, lots of special things have the form ``__NAME__``. We'll learn a few more of these special names today, and we'll meet many more in the last week of the course.

In the name of honesty, I should say that ``__init__`` isn't exactly like a constructor in, say, Java. If we're going to be precise, ``__init__`` is an **initializer**. But most developers go ahead and call ``__init__`` a constructor. Python's object construction works quite differently from in Java, and while it has something that you'd call a "constructor" like Java's, it's not usually necessary to think about it. None of this is very important, but it's good to have in the back of your mind that the waters here are a little deeper than we're making it seem.