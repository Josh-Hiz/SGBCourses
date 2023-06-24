Binary search
=============

Suppose we know something more about our list---that it's sorted ascending, i.e., each element is no smaller than the previous one (but maybe equal, if there are duplicates). Can we use that information to write a better search? Absolutely! Here's the intuition: suppose we're looking for the number 10 in a list of sorted numbers. We glance at the list and see the number 50. If the list is sorted ascending, we know that if 10 is in the list, it's to the left of 50---we can ignore everything to the right, since it's greater than or equal to 50 which is greater than 10.

The algorithm is called **binary search**, because we cut the elements we're looking at---the **range** of the list we're considering---in half every time. Here's the idea to find a needle/target element ``v`` in a list of ``n`` elements:

1. Start out with a lower bound of ``lo = 0`` and an upper bound of ``hi = n-1``. These define our current range.
2. Look at the middle element of our range (i.e., ``mid = lo + ((hi-lo) / 2)``), call it ``x``.
    (a) If ``v`` is equal to ``x``, return the index ``mid``.
    (b) If ``v`` is less than ``x``, set hi to ``mid-1``.
    (c) If ``v`` is greater than ``x``, set lo to ``mid+1``.
3. If ``hi < lo``, the element is not in the list.
4. Go back to (2).

Let's see it in Python:

.. runner:: 

    def binary_search(v, l):
        lo = 0
        hi = len(l) - 1
        while lo <= hi:
            mid = lo + ((hi - lo) // 2) # what goes wrong if we use / ?
    #        print(f'looking at {mid} between {lo} and {hi}')
            x = l[mid]
            if   v == x: return mid
            elif v <  x: hi = mid - 1
            elif v >  x: lo = mid + 1
        raise ValueError(f'{v} not found')

    l = [0,1,2,3,4,5,6,7,8,9,10]
    for x in l:
        assert binary_search(x, l) == l.index(x) # test using list.index

    binary_search(30, l)

If you're not sure why the code is working, try uncommenting the ``print`` call. It will tell you the values of ``mid``, ``lo``, and ``hi`` on every iteration.

Correctness here is harder to show---it's the sort of thing we'd talk about in a data structures or algorithms course. The general method is to go by **induction** on the length of the range, using the sortedness of the list to argue that everything above ``hi`` is strictly greater than ``v`` and everything below ``lo`` is strictly less than ``v``. At every step, our range shrinks, and we get closer to ``v`` (or its absence). In the **base case** of the induction, ``hi < lo``, and that means all elements in the list are either greater or less than ``v``, so ``v`` cannot be in the list---and we're correct to indicate "not found".

Performance
-----------

Binary search is a more complicated algorithm than linear search---it's very easy to get it wrong! But it comes with a huge advantage: it is **much** more performant. If your list is sorted, binary search is very much superior to linear search.

A deep analysis requires some more advanced tools (induction again, and some careful math). But we can sketch it out here, again using "number of comparisons" as our measure.

In the **best case**, our element is exactly in the middle. We found it on our first go, making only one comparison.

In the **worst case**, our element isn't in the list. How many elements will be consider? Each time we run the loop, our range halves. How many times can we run the loop before our range shrinks to nothing (i.e, ``hi < lo``) and we have to give up? The number of times you can halve a number corresponds to its logarithm base 2 a/k/a its binary logarithm, written:

.. raw:: latex

    log_{2}(n)

Logarithmic performance is *fantastic*. Why? Well, suppose we have 1000 elements. Linear search will perform 1000 comparisons before giving up. We'll perform ``log2(1000)`` comparisons. If you know that ``2**10 == 1024``, you can guess how many comparisons, but we can also just compute:

.. raw:: latex

    1000/2 = 500
    500/2 = 250
    250/2 = 125
    125/2 \approx 62
    62/2 = 31
    31/2 \approx 15
    15/2 \approx 7
    7/2 \approx 3
    3/2 \approx 1
    1/2 \approx 0

We can expect 10 comparisons before giving up. That's a *huge* improvement over linear search's 1000 comparisons! On 2000 elements, we'd have 11 comparisons, while linear search would do... 2000! Yikes!

Our **average case** resembles the worst case---given uniform distribution, we can expect to do no more than ``log2(n)`` comparisons.

Invariants
----------

It's very common to use an invariant like "the list is sorted" to find a better algorithm. Such invariants can be tricky to maintain, but often allow for much better performance. Such invariants are common not only in computer science, but all through the world: dictionaries are in sorted order to make it easy to find words; libraries use special categorizations to help you find the books you're looking for in particular; a restaurant menu is broken into sections to help you find foods that you're interested in.