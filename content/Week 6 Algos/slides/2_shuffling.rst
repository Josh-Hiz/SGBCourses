Shuffling: stating the problem
==============================

Our first algorithm will be the `Fisher-Yates shuffle <https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle>`_, which is also called the Knuth shuffle. Let's start by stating our problem clearly:
    
    A **shuffle** takes a sequence and rearranges the items in it randomly in place; each possibly arrangement has equal probability, i.e., the distribution of possible permutations is uniform.

There are a few surprising things here.

1. We didn't mention any particular data structure, just a "sequence" of "items".
2. We're using randomness in an algorithm! Aren't algorithms supposed to be finite and well-defined?
3. Our correctness criterion---a uniform distribution---isn't something you can directly observe.

Algorithms are abstract
-----------------------

It's common for algorithms to be very abstract. In fact, it's an advantage! By giving a very general description of a problem statement or an algorithm, more people may see how their problem may relate.

Randomness is well-defined
--------------------------

While our algorithm will use randomness, the steps themselves will be finite and well-defined in advance. Occasionally we'll use randomness to make a decision, but the set of decisions we'll be making is fixed in advance.

Correctness is hard
-------------------

Finally, knowing you got it right is the hardest part. Shuffling and other random algorithms are particularly challenging because randomness is a property of distributions not of values. We'll have to work extra hard to convince ourselves we got it right. In the ideal case, we'd do a *proof*, either on paper or maybe even checked by the computer itself.

