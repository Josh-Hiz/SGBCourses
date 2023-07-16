Comprehensions
==============

Python supports a concise notation called **comprehensions** for writing down for loops that generate data structures---you can think of it as a way of automatically combining ``map`` and ``filter``.

Here's a list comprehension:

.. runner::

    l = [0,1,2,3,4,5]
    squares = [x * x for x in l]
    print(squares)

You can use comprehensions with dictionaries and sets (which we haven't looked at). Here's an example with dictionaries:

.. runner::

    l = ["Michael", "Irfan", "Aditi"]
    names = {name: len(name) for name in l}
    print(names)

And here's one with sets (which are unordered groupings of unique elements, i.e. dictionaries with keys but no values):

.. runner::

    l = ["Michael", "Greenberg", "Michael", "Jackson"]
    names = {name for name in l}
    print(names)

You can put conditionals in a comprehension to get filtering:

.. runner::

    l = [0,1,2,3,4,5]
    squares = [x * x for x in l if x % 2 == 0]
    print(squares)

You can `read more about comprehensions in the Python data structure documentation <https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions>`_.