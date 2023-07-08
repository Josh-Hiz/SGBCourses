Testing types with isinstance
=============================

One common use of ``assert`` is to ensure that functions are called with the right types. For example, here's a ``mean`` function that checks that its inputs are (a) lists, and (b) non-empty. Uncomment some of the lines at the bottom to see how the program runs.

.. runner:: 

    def mean(l):
        assert isinstance(l, list), "mean expects a list"
        assert len(l) > 0, "mean expects non-empty lists"

        return sum(l) / len(l)

    #print(mean([1,2,3]))
    #print(mean("hello"))
    #print(mean(5))
    #print(mean([]))

Here we've used a special function, ``isintance``, which is for determining at runtime which values have which types.

``isinstance(v, t)``

Returns ``True`` if ``v`` has type ``t``, and ``False`` otherwise.

Defensive programming
---------------------

It's a good idea to get into a defensive mindset. Whenever you're writing a function, think to yourself: how could this go wrong? I expect certain inputs---types, subsets of those types, and so on. What could go wrong if my assumptions are violated? Using ``assert`` lets you protect yourself: if a failure happens due to an ``assert``, the person calling your function learns something important... they violated your assumptions!

Especially when working in teams, defensive programming helps ensure that pieces written by different people work together well. Checking your assumptions takes time, it's true: it takes time for you to write and test the code, and it takes time when the program is running. But if you don't check your assumptions, your program can do some pretty wacky things. Better to be sure!