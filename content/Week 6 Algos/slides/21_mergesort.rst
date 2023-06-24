Merge sort
==========

**Merge sort** is a divide-and-conquer approach to sorting that generates a new list. Like quicksort, it works by splitting the list in half. Unlike quicksort, the idea is quite simple:

* Split the list in two arbitrarily.
* Recursively sort each of the split lists.
* Merge the shorter, sorted lists into a single list.
  
Here's the pseudocode:

.. code-block:: 

    -- merge - merge two sorted lists into a single list
    merge(l1, l2):
        if l1 is empty: return l2
        if l2 is empty: return l1
        
        if l1[0] < l2[0]:
            return l1[0] followed by merge(l1[1:], l2)
        else:
            return l2[0] followed by merge(l1, l2[1:])
                    
    -- mergesort - sort a list l into a new list
    mergesort(l):
        split l arbitrarily into two lists l1 and l2 of nearly equal length
        l1_sorted = mergesort(l1)
        l2_sorted = mergesort(l2)
        return merge(l1_sorted, l2_sorted)

For the split, we can do something simple: copy every other element to one of two lists. Let's try it in Python:

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

        ls = split(l)

        l1 = mergesort(ls[0])
        l2 = mergesort(ls[1])

        return merge(l1, l2)

    l = [3,1,6,2,9,5,0,4,8,7]
    print(mergesort(l))

    l = [3,1,6,2,9,5,0,4,8,7,5,4,6,3,7,2,8,1,9,0]
    print(mergesort(l))

    l = [1,1,3,1,1,1]
    print(mergesort(l))

    l = [1,1,1,1,1,100]
    print(mergesort(l))

Correctness
-----------

The correctness of merge sort is substantially easier to see than for quicksort. The ``split`` procedure is more or less arbitrary, and produces lists that are approximately half the list in length. The ``merge`` procedure will clearly produce a sorted list from two sorted lists: each time it picks off the lowest element on the front of the two lists. The ``mergesort`` procedure itself is quite simple: it splits the list, sorts them (guaranteed to be correct by an inductive argument), and then merges them.

Performance
-----------

Merge sort will produce recursions with a perfect tree pattern: each recursive call splits the list in half. We don't have to worry about pivot elements the way that quicksort does. We'll get the ``n * log2(n)`` comparisons every time.

One big difference with quicksort is that merge sort produces new lists---and by default, it produces quite a few of them! It's possible to use less space than our implementation: in general, to merge sort a list of ``n`` elements, you need to allocate space for another ``n`` elements. Our code allocates as it goes, and the merge will allocate again.

Our ``split`` routine splits every other item. In Python, it'd be easy enough to define a simpler split as, e.g., ``(l[0:len(l)//2], l[len(l)//2:])``. Efficient implementations may use ranges of the original list and do some work in place.