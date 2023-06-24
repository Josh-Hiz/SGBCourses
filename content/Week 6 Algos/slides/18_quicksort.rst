Quicksort
=========

Our last two sorting algorithms are the two most popular algorithms in practice. First, let's look at **quicksort**.

Quicksort is a very fast in-place sort. It works via **divide-and-conquer**. The intuition is the following two-phase approach:

* In the **partition phase**: swap the elements of the array around a **pivot element**: everything to the left in the list should be less than the pivot and everything to the right should be no less than the pivot.
* In the **recursion phase**: sort each partition independently by recursively calling quicksort.

The idea is similar to binary search. Binary search shows gains over linear search by only looking at half the input once. Here, we will look at all of the input eventually---but the partition phase reduces the amount we have to look at in any given pass by half. Here's the pseudocode:

.. code-block:: 

    -- partition - arrange a list around a pivot value and lower and upper bounds
    --             returns the index of where the pivot ends up
    partition(l, pivot, lo, hi):
    # start out of bounds
    lo = lo - 1
    hi = hi + 1
    
    loop:
        increment lo until l[lo] >= pivot
        decerement hi until l[hi] <= pivot
        
        if lo > hi: stop and return hi
        
        swap l[lo] and l[hi]

    -- quicksort - sort a list l inplace between indices lo and hi
    quicksort(l, lo, hi):
    if lo < 0 or hi >= length of l or lo >= hi: stop

    choose a pivot value from the list
    p = partition(l, pivot, lo, hi)
    quicksort(l, lo, p)
    quicksort(l, p+1,hi)

The quicksort routine itself is simple: partition the list around the pivot, and then sort the remaining parts. The partition is harder to understand. The idea is to start with the bounds and work the ``lo`` and ``hi`` bound down until you find an **inversion**, i.e., ``l[lo] > pivot`` and ``l[hi] < pivot``. These elements need to be swapped to have the list partitioned correctly! We keep processing inversions until the bounds pass each other, i.e., we've considered the whole range. The `Wikipedia article has a nice animation of this process <https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme>`_.

We've left off some detail about how to choose the pivot element. Let's start with a simple scheme, where we just use the middle element of the list. Here's the Python code:

.. runner:: 

    def swap(l, i, j):
        if i == j: return

        tmp = l[i]
        l[i] = l[j]
        l[j] = tmp

    def partition(l, pivot, lo, hi):
    #    print(f'partition({l[lo:hi+1]}, {pivot}, {lo}, {hi})')

        while True:
            while l[lo] < pivot:
                lo = lo + 1

            while l[hi] > pivot:
                hi = hi - 1

            if lo >= hi: return hi

            swap(l, lo, hi)

            # make sure the next round skips past these swapped values
            lo = lo + 1
            hi = hi - 1

    def quicksort_range(l, lo, hi):
        if lo < 0 or hi < 0 or lo >= hi: return
    #    print(f'quicksort({l[lo:hi+1]}, {lo}, {hi})')
        pivot = l[lo + ((hi - lo) // 2)]
        p = partition(l, pivot, lo, hi)
        quicksort_range(l, lo, p)
        quicksort_range(l, p+1, hi)

    def quicksort(l):
        quicksort_range(l, 0, len(l) - 1)

    l = [3,1,6,2,9,5,0,4,8,7]
    quicksort(l)
    print(l)

    l = [3,1,6,2,9,5,0,4,8,7,5,4,6,3,7,2,8,1,9,0]
    quicksort(l)
    print(l)

    l = [1,1,3,1,1,1]
    quicksort(l)
    print(l)

    l = [1,1,1,1,1,100]
    quicksort(l)
    print(l)

It may be edifying to uncomment the internal ``print`` calls, which will tell you about every call being made.

Correctness
-----------

The ``partition`` function is *very* subtle, and it's easy to get things wrong! It took me twenty minutes to debug this version---even with a correct reference in front of me!

The intuition for correctness is that when ``partition`` with a given ``pivot`` returns an index ``p``, then everything to the left of ``p`` is less than ``pivot``, and everything to the right is no smaller. An inductive argument uses this fact about ``partition`` to show that the list will be sorted.

Performance
-----------

A full analysis of quicksort is somewhat demanding. In the best and average cases, you can think of recursion making a tree: the root is the outer call to quicksort; each time recursive calls happen, the list cuts in half. As we saw for binary search, this will give us a tree of height ``log2(n)``, where ``n`` is the length of the list. Each element in the list appears in just one "leaf" of this tree (the very last recursive calls, where the list is of length 1 or 2); that element is considered on every call from the leaf back to the root, and it could be swapped every time. So we can expect ``n * log2(n)`` swaps to do a sort.

The ``log2`` analysis depends on the partitions being of roughly equal size each time---and that depends on our list. In the worst case, we could choose a terrible pivot every time: every element is less or greater than that pivot. In that case, our tree would have height ``n``, and we'd do ``n * n``, i.e., ``n ** 2`` swaps. A lot depends on the pivot!