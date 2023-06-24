Sortedness
==========

Before we introduce our next algorithm, we need to take a brief detour to talk about **sortedness**.

We say a list is **sorted** when each element is no smaller than the previous one. Let's unpack that definition:

1. If our list is ``[x, y, z]``, then it must be that ``x <= y`` and ``y <= z`` (so ``x <= z`` transitively).
2. By default, sortedness means **sorted ascending**.
3. The empty list is trivially sorted, e.g., ``[]`` is sorted.
4. A list with one element is trivially sorted, e.g., ``[47]`` is sorted.
5. Sorted lists can have duplicates, e.g., ``[0,1,1,2,2,2]`` is sorted ascending.
   
People sometimes refer to other notions of sorting, like sorted descending or sorted on a particular aspect (e.g., sorting by last name and then first name). But if nothing else is specified, the default is to sort ascending.
