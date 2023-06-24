Linear search
=============

Linear search is the simplest search algorithm: look at each item in turn and see if it matches. Here's pseudocode:

.. code-block:: 

    -- linear search to find a needle/target element v in a list l
    for each element x at index i of l:
    if x matches the target v:
        return i
    return not found

Here it is in Python:

.. runner:: 

    def linear_search(v, l):
        i = 0
        for x in l:
            if x == v:
                return i
            i = i + 1
        raise ValueError(f'{v} not found')

    print(linear_search(5, [20, 15, 10, 5, 0]))
    print(linear_search(5, [19, 14, 9, 4, 0]))

Performance
-----------

It's common to analyze algorithms in terms of **best case**, **worst case**, and **average** or **expected** performance. Rather than speaking in terms of time, we can speak in terms of "number of values looked at" or "number of comparisons", which should be a pretty good proxy for the time our algorithm takes.

In the **best case**, the value we're looking for is at the front of the list, e.g., ``linear_search(5, [5,10,15,20,25])``. We'll look at one element and---tada! We're done.

In the **worst case**, the value we're looking for isn't in the list at all, e.g., ``linear_search(5, [19, 14, 9, 4, 0])``. We have to look at every single element in the list; if the list has ``n`` elements, we'll perform ``n`` comparisons.

In the **average case**, we might assume that the elements are uniformly distributed through the list or not present, i.e., each index is as probable as each other one and as probable as not being there. Here we'll have to look at about half the list on average; if the list has ``n`` elements, we'll perform ``n/2`` comparisons (plus or minus one, depending on even/oddness of the list).

Duplicates
-----------

What happens if there are duplicates in the list? Think to yourself about this before reading on.

Done thinking? Here, we'll return the leftmost index. There's no "correct" answer here---one might reasonably want the rightmost index. It's important, however, to make the policy clear so that people can think clearly about what they need for their code.