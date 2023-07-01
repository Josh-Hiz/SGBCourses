Objects and classes: recap
==========================

We have learned quite a bit of new stuff in Python! Let's go over it again.

* **Classes** are a way of naming **types** in Python.
* **Objects** package code and data together; every Python object has a class.
* You define a new class by writing ``class Name(Base): ...``, where ``Name`` is the name of your new class and ``Base`` is its base class.
* So far, ``object`` is the only base class we've used.
* You can set a **field** on an object by saying ``o.field = ....`` You can read it by just writing ``o.field``.
* Putting a ``__`` before a field name marks it as private, and makes it hard to refer to.
* The body of a class definition contains **method** definitions.
* The ``__init__`` method defines a **constructor**, i.e., an object that is a new **instance** of the class.
* Every method takes ``self`` as the first argument.
* You can define whatever other methods you want, in whatever order.
* The ``__str__`` method says how to convert an object to a string for, e.g., printing.
* The ``__repr__`` method says how to convert an object to a string representation of the Python value.

Whew! That's a lot of mechanism compared to, "here's how to define a function and call it". We'll spend the rest of today looking at some of the object-oriented ecosystem in Python, with a focus on navigating the world and doing testing. OOP is complicated, but it also makes many hard things easier and some otherwise impossible things possible. (We won't address it in this course, but OOP is a lynchpin technology for user interfaces.)