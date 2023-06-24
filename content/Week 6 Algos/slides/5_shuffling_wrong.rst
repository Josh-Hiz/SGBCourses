Shuffling wrong
===============

Why is Fisher-Yates right? It's a very particular loop. (The following is drawn from a `nice analysis by Mike James <https://www.i-programmer.info/programming/theory/2744-how-not-to-shuffle-the-kunth-fisher-yates-algorithm.html>`_.) We might write something instead like:

.. code-block:: 

    -- To shuffle an array a of n elements (indices 0..n-1):
    for i from 0 to n-1 inclusive do
        j ← random integer between 0 and n-1, inclusive
        exchange a[j] and a[i]

First: how is this different?

Second: what's wrong with it? If you wrote this up in Python and looked at the output, it would certainly look random. But it turns out that its output is biased, generating certain orderings more often than others. Our problem statement of shuffling asked for a uniform distribution, so bias is a bug! `James's post <https://www.i-programmer.info/programming/theory/2744-how-not-to-shuffle-the-kunth-fisher-yates-algorithm.html>`_ goes into this in some detail.

There are two ways we could find out that this algorithm is wrong. The *hard way* is to do a thoroughgoing, exhaustive analysis the way James does. The *not quite as hard* way is to test our code extensively enough that we can have some confidence that we got it right.

Exhaustive analysis
-------------------

To do an exhaustive analysis (like James), we would want to explore every possible output of our algorithm---here, to ensure that we're getting a uniform distribution. One option would be to write a program like the following, which is *like* a shuffle, but instead records every permutation it could generate:

.. runner:: 

    import random

    def swapped(l, i, j):
        l_swapped = list(l)
        l_swapped[i] = l[j]
        l_swapped[j] = l[i]
        return l_swapped

    def shuffle_next(l, i):
        res = []
        for j in range(0, i+1):
            res.append(swapped(l, i, j))
        return res

    def all_shuffles(l_orig):
        i = len(l_orig) - 1
        possibilities = [l_orig]
        while i >= 1:
            next_possibilities = []
            for l in possibilities:
                # record all possible shuffles of existing possibilities
                next_possibilities.extend(shuffle_next(l, i))
            possibilities = next_possibilities
            i = i - 1
        return possibilities

    print(all_shuffles(list("")))
    print(all_shuffles(list("A")))
    print(all_shuffles(list("AB")))
    print(all_shuffles(list("ABC")))

    def fact(n):
        res = 1
        while n >= 2:
            res = res * n
            n = n - 1
        return res
        
    s = "ABCDEF"
    for i in range(len(s)+1):
        print(f'{i} {fact(i)} {len(all_shuffles(s[:i]))}')
        assert fact(i) == len(all_shuffles(s[:i]))

This code is somewhat complex, and is only indirectly doing what ``shuffle`` did. The ``swapped`` function returns a *new* list, with positions swapped. The ``shuffle_next(l, i)`` function computes all of the shuffles of ``l`` when at index ``i``. The ``all_shuffles`` function is more complicated: it starts with one possibility, and then for each ``i``, it computes every possible resulting shuffle.

Looking at the output of ``all_shuffles``, we can see that there are no repeats---that's great news! We can even write a test to see that running ``all_shuffles`` on a list of length ``n`` will yield ``n!`` (i.e., ``fact(n)``) possible answers.

Let's do the same for our broken shuffle (look for "CHANGED HERE" for the critical line):

.. runner:: 

    import random

    def swapped(l, i, j):
        l_swapped = list(l)
        l_swapped[i] = l[j]
        l_swapped[j] = l[i]
        return l_swapped

    def broken_shuffle_next(l, i):
        res = []
        for j in range(0, len(l)): # CHANGED HERE
            res.append(swapped(l, i, j))
        return res

    def broken_all_shuffles(l_orig):
        i = len(l_orig) - 1
        possibilities = [l_orig]
        while i >= 1:
            next_possibilities = []
            for l in possibilities:
                # record all possible shuffles of existing possibilities
                next_possibilities.extend(broken_shuffle_next(l, i))
            possibilities = next_possibilities
            i = i - 1
        return possibilities

    print(broken_all_shuffles(list("")))
    print(broken_all_shuffles(list("A")))
    print(broken_all_shuffles(list("AB")))
    print(broken_all_shuffles(list("ABC")))

    def fact(n):
        res = 1
        while n >= 2:
            res = res * n
            n = n - 1
        return res
        
    s = "ABCDEF"
    for i in range(len(s)+1):
        print(f'{i} {fact(i)} {len(broken_all_shuffles(s[:i]))}')
    #    assert fact(i) == len(all_shuffles(s[:i]))

Aha! You can see that once we have three elements, we start to see some repeated elements (e.g., ``['A', 'C', 'B']`` shows up twice). That means there are more random choices that produce those permutations, which means we're not uniform!

Empirical testing
-----------------

Exhaustive analysis has some weaknesses. The biggest weakness here is that to exhaustively test our random algorithm, we had to rewrite it to be a different, not random algorithm. It's now hard to be confident that the non-random code is the right model for the random code! It's also a lot more work to write up this new algorithm.

To do empirical testing, we'll come up with ways to run our code as-is, but in a way that gives us confidence. For shuffles, there's an easy solution: just do it a lot, and then look at the distribution. If there's bias, we should be able to see it!