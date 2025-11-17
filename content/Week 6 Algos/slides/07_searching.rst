Searching
=========

With one algorithm under our belt, let's learn two more: searching.

A **search algorithm** takes a **needle** and a **haystack**: the **needle** is something to look for, and the **haystack** is the thing we're looking in. For now, we'll focus on searching for **values** in **lists**, i.e., we'll ask questions of the form "is value ``x`` in the list ``l``?". Before reading on... what else might we want to search for?

What should a search algorithm return? Sometimes, it's enough to return a boolean, saying, "yes, it's in there". More generally, we want to know *where* the value is, returning an index or other way of finding the value; if the value can't be found, we'll signal the problem using a ``ValueError`` or a **sentinel value** that indicates "not found".

Alternative searches
--------------------

We might also want to search for values that meet some predicate (i.e., if ``f`` takes values to booleans, we want to find a value ``x`` in ``l`` such that ``f(x)`` is ``True``), or we might want to collect every value in some range of values (e.g., numbers between ``0`` and ``15``). It's not hard to adapt a search to work with a predicate; **range queries** often depend on particular data structures.
