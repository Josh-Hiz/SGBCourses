Choosing the pivot element
==========================

Our first cut at quicksort chose the pivot element as the middle of the array. That choice turns out to be important for the partition function we use (following `Tony Hoare's <https://en.wikipedia.org/wiki/Tony_Hoare>`_ original scheme), since the function will behave erratically if the pivot we choose is the end of the array and all other elements are less than it.

There are other problems, too: what if the pivot element we pick every time happens to be largest or smallest element in the array? Then each time one partition will have just one element, and we'll do ``n ** 2`` swaps. The choice of pivot matters quite a bit.

One popular choice is the *random* pivot: just randomly pick an element from the array as the pivot. It's very, very unlikely to choose a bad pivot every time, so things should work out on average. One disadvantage is that randomness brings nondeterminism, i.e., your code won't behave exactly the same every time. That makes it much harder to test (as we saw for the Fisher-Yates shuffle).

There are also other partition schemes, which adapt better to having many duplicate values. So-called **fat partitions** use a three-way partition: items less than the pivot, items equal to the pivot, and items greater than the pivot. Treating equal items differently makes it easier to have a stable sort (where elements retain their relative ordering) and also reduces the size of the other partitions during recursive calls.