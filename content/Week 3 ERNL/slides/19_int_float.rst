Surprise: integers and floats are unrelated
===========================================

So far, we've freely mixed ``int``'s and ``float``'s. But in Python, they're actually just totally different things. Look: ``5`` isn't a float and ``5.0`` isn't an ``int``.

.. runner::

    print(isinstance(5, float))
    print(isinstance(5.0, int))

It turns out that Python is happy to silently and automatically convert between ``int`` and ``float`` for you, even though the types aren't directly related.