Surprise: bools are numbers!
============================

While you might have been surprised that ``int`` and ``float`` aren't related types, you'll be even more surprised to learn that ``bool`` is closely related to ``int``:

.. runner::

    print(isinstance(True, int))
    print(isinstance(False, int))

What? A ``bool`` is an ``int``? Like the C language before it, Python says that ``1`` and ``True`` are equivalent, and ``0`` and ``False`` are equal. Look:

.. runner::

    print(True == 1)
    print(False == 0)

    print(True == 2)

Observe, however, that ``True`` is equal to ``1`` but is not the *same thing* as 1:

.. runner::

    print(True is 1)
    print(id(True))
    print(id(1))

    print(False is 0)
    print(id(False))
    print(id(0))

(Nevermind the warnings: they're just saying that it doesn't usually make sense to use ``is`` when both sides are literals.)

We can see the relationships between ``bool`` and ``int`` in another light: every ``bool`` is an ``int``, but not the otherway round (e.g., ``2`` is "truthy", but it's not equal to ``True`` like ``1`` is). We say that ``bool`` is a **subclass** or **subtype** of ``int``. There's a Python function that helps here:

.. runner::

    print(issubclass(bool, int))
    print(issubclass(int, bool))

``issubclass(t1, t2)``

Returns ``True`` when ``t1`` is a subclass of ``t2``; returns ``False`` otherwise.