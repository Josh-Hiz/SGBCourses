Strings and Lists in Python
===========================

Throughout this module and the previous module on strings, you might have noticed several similarities between strings and Lists in Python. The following operations work the same way in strings and lists: indexing, slicing, and ``len`` function to compute the length of a string or of a list. However, strings are not interchangeable with lists because of some important differences. We can say that strings are a sequence of characters only, whereas lists can be a collection of any data type (or more than one type!).

We can always say that a String is a sequence of characters and we can even type convert a string to a list using the ``list()`` function. More on this later.

One important difference between strings and list is that you can update the elements in a list using their indices (e.g., ``lst[1] = 30``). However, the same cannot be done with strings as they are immutable. You will learn more about mutable and immutable data types in the later modules.

