Insertion sort: the "natural" sort
==================================

Our first and simplest sort is **insertion sort**. Insertion sort takes a list and returns a **new, sorted** list that's a permutation of its input.

Insertion sort depends on two simple recursive functions: ``insertion_sort`` does the sorting, and ``insert_sorted`` takes an element ``v`` and a *sorted* list ``l`` and puts ``v`` in the right place. Here's the algorithm:

.. code-block:: 

    -- insertion sort on a list l
    insertion_sort(l):
        if l is empty, return the empty list
        split l into the first element x and the rest l'
        return insert_sorted(x, insertion_sort(l'))

So simple! The intuition is that ``res`` is always sorted, and each time we insert ``x`` into ``res``, we get a new, longer sorted list back. If we do that for every element in ``l``, we're done. The critical question is: how does ``insert_sorted`` work?

.. code-block:: 

    -- insert_sorted takes an element v and a SORTED list l
    -- returns a new list, with v in the right place
    insert_sorted(v, l):
        if l is empty:
            return the list containing just v
        x = first element of l
        if v < x:
            return v followed by l
        otherwise:
            return x followed by insert_sorted(v, l'), where l' is the rest of l after y

Let's see it in Python code:

.. runner::

    def insert_sorted(v, l):
        if len(l) == 0: return [v]
        x = l[0]
        if v < x:
            return [v] + l
        else:
            return [x] + insert_sorted(v, l[1:])

    def insertion_sort(l):
        if len(l) == 0:
            return []
        else:
            return insert_sorted(l[0], insertion_sort(l[1:]))

    print(insertion_sort([10,0,8,5,3,9,2,7,1,4,6]))
