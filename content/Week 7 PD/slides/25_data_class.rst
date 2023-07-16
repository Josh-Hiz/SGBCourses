Document field names and types with data classes
================================================

Python's **data classes** let you write classes that look more like classes in languages like C++ or Java, where you declare each member field's type in advance. You use a decorator and write some type annotations, and you'll get nice ``__init__`` and ``__repr__`` methods (among other things) automatically. Here's an example:

.. runner::
    from dataclasses import dataclass

    @dataclass
    class Person(object):
        name: str
        cwid: int
        role: str

        def is_professor(self):
            return 'professor' in self.role

    mg = Person(name = 'Michael Greenberg', cwid = '20005138', role = 'Assistant professor')
    print(mg)
    print(mg.name)


Data classes provide good documentation (field names and types!).