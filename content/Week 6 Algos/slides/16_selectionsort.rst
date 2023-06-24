Selection sort
==============

**Selection sort** works by finding the minimum element of the list each time and **swapping** elements to get the list sorted. Where insertion sort creates a new list, selection sort is an **in place** algorithm.

Here's some pseudocode:

.. code-block:: 

    -- selection sort - sort a list l of length n in place
    selection_sort(l):
    for each index i in 0 ... n - 2 inclusive:
        j = minimal element in range i ... n - 1 inclusive
        swap i and j

Why does this work? Let's imagine we're sorting a list ``[4,3,1,2]``. What happens?

* First, ``i`` is 0. We find the minimal element in the range 0 to ``n-1``, i.e., of the whole list. The minimum is 1, and it's at index 2. So we swap indices 0 and 2, and our list is now ``[1,3,4,2]``.
* Now ``i`` is 1. We find the minimal element in the range 1 to ``n-1``, i.e., leaving out index 0, which we know is sorted. The minimum is 2, and it's at index 3. So we swap indices 1 and 3 and our list is now ``[1,2,4,3]``.
* Now ``i`` is 2. We find the leftmost minimal element in the range 2 to ``n-1``, i.e., leaving out indices 0 and 1, which are know are sorted. The minimum is 3, which is at index 3 (after the last swap). So we swap indices 2 and 3 and our list is now ``[1,2,3,4]``.
* We're done! We don't need a loop for the last index, because everything to the left is sorted and was less than this element.

The intuition for correctness here is that at the end of iteration ``i``, everything up to ``i`` is sorted, and everything to the right is no less than everything up to ``i``.

For performance, selection sort does a lot of comparisons: each element is compared to the rest of the list. If the list is of length ``n``, we'll do ``n ** 2`` comparisons. That turns out to be on the high side for sorting. But thw good news is that we'll do at most ``n-1`` swaps---one per iteration. (If ``i`` and ``j`` are the same---i.e., the minimal element is already in the right spot---we don't need to actually swap anything.) So if it was cheap to compare elements but expensive to swap them, selection sort could be a great fit.

Let's see it in Python:

.. runner:: 

    def swap(l, i, j):
        if i == j: return

        tmp = l[i]
        l[i] = l[j]
        l[j] = tmp

    def find_minimum(l, start):
        assert 0 <= start < len(l)

        min_idx = start
        min_val = l[start]

        for i in range(start+1, len(l)):
            val = l[i]
            if val < min_val:
                min_idx = i
                min_val = val
            i = i + 1
        return min_idx

    def selection_sort(l):
        for i in range(len(l) - 1):
            j = find_minimum(l, i)
            swap(l, i, j)

    l = [3,1,6,2,9,5,0,4,8,7]
    selection_sort(l)
    print(l)