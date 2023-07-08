Errors from partial operations
==============================

Even well typed operations can fail. Division is the canonical *partial* operation, since it's not defined when the divisor is 0. Here's an example:

.. runner:: 

    print('hello')

    def two_divided_by(n):
        return 2.0 / n

    print('the result is', two_divided_by(5))
    print('the result is', two_divided_by(0))

    print('goodbye')

Here we get a ``ZeroDivisionError``. Just like ``TypeError``'s and ``NameError``'s, errors like division by zero can be latent. Every programming language in common use has latent errors in partial operations.

We've seen other partial operations, like ``list.index``. Here's another example:

.. runner:: 

    l = "twas brillig and the slithy toves did gyre and gimble in the wabe".split(' ')

    print('brillig is at index', l.index('brillig'))
    print('jabberwocky', l.index('jabberwocky'))

Here we get a ``ValueError`` when we try to find the index of an item not in the list.

Finally, list and string indexing is partial and can produce errors:

.. runner:: 

    l = "all mimsy were the borogroves and the mome raths outgrabe".split(' ')

    print('index 4 is', l[4])
    print('index 10 is', l[10])

Here, we get an ``IndexError``. We'd get it for string indexing too:

.. runner:: 

    s = "beware the jabberwock, my son; the jaws that bite, the claws that catch"

    print('index 4 is', s[4])
    print('index 100 is', s[100])

Notice that the messages accompanying the ``IndexError`` are slightly different: each message mentions the type that was being indexed.