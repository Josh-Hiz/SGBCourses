Unpacking patterns
==================

We've generally written Python assignment statements that have only one thing to the left of the ``=`` sign. But you can write more complex assignments that **unpack** the values on the right-hand side.

Here's an example from ``mergesort``:

.. runner::

    def merge(l1, l2):
        if len(l1) == 0: return l2
        if len(l2) == 0: return l1

        if l1[0] < l2[0]:
            return [l1[0]] + merge(l1[1:], l2)
        else:
            return [l2[0]] + merge(l1, l2[1:])

    def split(l):
        left = []
        right = []

        go_left = False
        for x in l:
            if go_left:
                left.append(x)
            else:
                right.append(x)

            go_left = not go_left

        return (left, right)

    def mergesort(l):
        if len(l) < 2: return list(l)

        ls = split(l) # XXX

        l1 = mergesort(ls[0])
        l2 = mergesort(ls[1])

        return merge(l1, l2)

At the line marked ``XXX``, we name the result of ``split``---which should be a tuple of lists. We save this tuple as ``ls`` and then then index it below. We can use **unpacking** to simplify things:

.. runner::

    def merge(l1, l2):
        if len(l1) == 0: return l2
        if len(l2) == 0: return l1

        if l1[0] < l2[0]:
            return [l1[0]] + merge(l1[1:], l2)
        else:
            return [l2[0]] + merge(l1, l2[1:])

    def split(l):
        left = []
        right = []

        go_left = False
        for x in l:
            if go_left:
                left.append(x)
            else:
                right.append(x)

            go_left = not go_left

        return (left, right)

    def mergesort(l):
        if len(l) < 2: return list(l)

        (l1, l2) = split(l) # XXX

        l1 = mergesort(l1)
        l2 = mergesort(l2)

        return merge(l1, l2)

    print(mergesort([5,3,1,4,2,7,0,8,9,6]))

Notice how much more concise and clear the code is! Unpacking is a great way to simplify your code. You can do fancier things, too:

.. runner::

    first,*middle,last = range(0,10)
    print(first)
    print(middle)
    print(last)

The ``*`` is a bit like ``*args``---it captures "everything else" as a list. You can only put one star in any unpacking statement.