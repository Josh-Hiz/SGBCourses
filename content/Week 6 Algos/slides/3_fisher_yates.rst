The Fisher-Yates shuffle
========================

We want to implement a **shuffle**.

    A **shuffle** takes a sequence and rearranges the items in it randomly in place; each possibly arrangement has equal probability, i.e., the distribution of possible permutations is uniform.

We'll implement the Fisher-Yates shuffle, as modernized by Don Knuth and Richard Durstenfeld. Here's the **pseudocode** from Wikipedia:

.. code-block::

    -- To shuffle an array a of n elements (indices 0..n-1):
    for i from n−1 downto 1 do
        j ← random integer such that 0 ≤ j ≤ i
        exchange a[j] and a[i]

Pseudocode is *almost* code, but it's a little less formal---a little less interested in the details of how things work. No programming language has exactly the syntax above, but it clearly communicates the idea to a human. It's also common to write prose-based instructions. Here's the same idea.

To shuffle a sequence of ``n`` elements (0-based indexing):

    1. For each index ``i`` from the last (index ``n-1``) element to the second (index ``1``):
        1. Let ``j`` be a number between ``0`` and ``i``, inclusive
        2. Swap element ``i`` and element ``j``.

So the last element (index ``n-1``) could swap with any element in the list---including itself! Then the second-to-last element (index ``n-2``) could swap with anything but the already-swapped last element. The third-to-last (index ``n-3``) could swap with anything but those last *two* elements. When we get down to the second element (index ``1``), it could swap with index ``0`` or itself. Our loop never touches index ``0`` directly in ``i``---only (possibly) in ``j``.

Here's an implementation in Python. What can you do to convince yourself that it's correct?

.. runner:: 

    import random

    def swap(l, i, j):
        tmp = l[i]
        l[i] = l[j]
        l[j] = tmp

    def shuffle(l):
        # or: for i in range(len(l) - 1, 0, -1):
        i = len(l) - 1
        while i >= 1:
            j = random.randint(0, i) # randint is inclusive
            swap(l, i, j)
            i = i - 1

    l = [1,2,3,4,5,6,7,8,9]
    print(l)
    for i in range(3):
        shuffle(l)
        print(l)