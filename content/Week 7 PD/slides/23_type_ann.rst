Type annotations
================

Python supports `type annotations <https://docs.python.org/3/library/typing.html>`_ in many positions. Here's an example:

.. runner::

    def factorial(n: int) -> int:
        res = 1
        while n >= 2:
            res *= n
            n -= 1
        return res

    print(factorial(5))

The type annotations above indicate that ``n`` is supposed to be an ``int`` and that ``factorial(n)`` will return an ``int``.

**Python does not actually enforce types in any way**. If we called ``factorial('hi')``, the code will run and we'll get an error (where?). Tools like `mypy <https://mypy-lang.org/>`_ help you find type errors. There's been a lot written about types, but http://veekaybee.github.io/2019/07/08/python-type-hints/ is a good place to start.