Enumerations of fixed values
============================

Python supports `enumerations as of Python 3.4 <https://docs.python.org/3.4/library/enum.html>`_; an **enumeration** is a handy way to identify some distinct values that are important. Here's an example where we enumerate flavors of milkshave:

.. runner::

    from enum import Enum

    class Milkshake(Enum):
        chocolate = 1
        strawberry = 2
        vanilla = 3

    for flavor in Milkshake:
        print(flavor)

    swirl = (Milkshake.chocolate, Milkshake.vanilla)
    print(swirl)
    print(Milkshake.chocolate.name, Milkshake.chocolate.value)
    print(Milkshake.chocolate == 1, Milkshake.chocolate.value == 1)

Notice that ``Milkshake`` subclasses ``Enum`` (which we imported from ``enums``). The ``Milkshake`` *class itself* is iterable, which is very convenient for when you have a finite set of options. Python gives us a nice way to access the name and value of an enumerated item, and gives us a good notion of equality.