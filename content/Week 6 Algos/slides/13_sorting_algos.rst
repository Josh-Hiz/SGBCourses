Sorting algorithms
==================

In the remainder of today's readings, we'll study sorting algorithms, i.e., algorithms which take in an arbitrary list (possibly sorted, but probably not) and yield a **sorted list** that is a **permutation of the original list**.

You might wonder about the second condition---what do we mean by a permutation of the original list, and why do we care? If we left off the second condition about permutations, the following would be a valid sort:

.. runner:: 

    def trivial_sort(l):
        return []
    
It's a very efficient sort---we do *no comparisons at all!* Nobody would seriously offer ``trivial_sort`` as a sorting algorithm, but without the second condition it would be 'correct'. More realistically, a sort implementation might accidentally drop (or add) duplicate elements---and *that* would be incorrect, too.

Different sorts take different approaches, with interesting properties beyond our scope in this course (e.g., stability---do duplicate items retain their relative ordering in the list?). More importantly, some sorting algortithms are **in-place** while others produce **new lists**. Neither is the "right one"---it depends on circumstance which approach is best. Python's ``list.sort`` is in-place.

