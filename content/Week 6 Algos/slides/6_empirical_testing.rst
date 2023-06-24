Empirically testing shuffle implementations
===========================================

We've defined two functions for you in ``task.py``: ``fisheryates`` and ``broken``. They're both purportedly shuffles, but we'd like to prove that they aren't.

Here's our plan: run each shuffle many, many times. We'll compute the distribution of the results and do some analysis on it. Concretely:

1. Pick a simple list---say, ``list("ABC")``, i.e.,  ``['A', 'B', 'C']``. There are 3! = 6 possible permutations.
2. Run ``fisheryates`` and ``broken`` 6000 times on ``list("ABC")``. Each permutation should show up about 1000 times, but there will be some variation.
3. Compute the histogram: how many times does each possible output appear?
4. Analyze the histogram: what are the mean, median, and standard deviation of the various frequencies.

Our tool produces output like:

.. code-block:: 

    fisheryates:
    ABC: 1014
    ACB: 944
    BAC: 1028
    BCA: 949
    CAB: 999
    CBA: 1066

    MEAN: 1000.0 MEDIAN: 1006.5 STDDEV: 22.861904265976328

    broken:
    ABC: 1299
    ACB: 1316
    BAC: 677
    BCA: 676
    CAB: 1338
    CBA: 694

    MEAN: 1000.0 MEDIAN: 996.5 STDDEV: 124.92397688194208

From this output, it's really clear that the ``broken`` function is indeed broken and ``fisheryates`` is good. It's worth noting that the mean and median aren't informative, but the distributions themselves and the standard deviations are very informative.

So: **test these two functions enough to determine that fisheryates is a shuffle and broken is not.**

We wrote a testing function ``test_shuffle`` that takes in a function and a list, and does the following:

1. Prints out ``f.__name__`` (which is the name of the function---cool!)
2. Runs ``fact(l) * 1000`` tests, shuffling a copy of the input list.
3. Stores the shuffled list in a dictionary, where the key is the list converted to a string (using ``''.join()``) and the value is the number of times that list has been seen.
4. Prints out the keys and their counts (sorted by key).
5. Prints out the statistics.

You don't need to do all of that, but it's good practice to write good, thorough tests like this! The more you do it, the easier it gets. To replicate our output, you'll have to write a number of helper functions: ``mean``, ``median``, and ``stddev``. We also defined ``fact`` so we could vary how many tests we compute with the length of ``l``.

.. challenge:: 

    import random

    def swap(l, i, j):
        tmp = l[i]
        l[i] = l[j]
        l[j] = tmp

    def fisheryates(l):
        # or: for i in range(len(l) - 1, 0, -1):
        i = len(l) - 1
        while i >= 1:
            j = random.randint(0, i) # randint is inclusive
            swap(l, i, j)
            i = i - 1

    def broken(l):
        # or: for i in range(len(l) - 1, 0, -1):
        i = len(l) - 1
        while i >= 1:
            j = random.randint(0, len(l) - 1) # 🤪
            swap(l, i, j)
            i = i - 1
