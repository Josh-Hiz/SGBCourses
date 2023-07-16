Decorators change behavior
==========================

Python's **decorators** are special markers that cause Python to treat your code differently. Decorators let you express common idioms easily, and they're used all over Python code in the real world.

There are many reasons to use decorators; one example is to automatically cache the results of functions. Suppose we are defining ``factorial`` recursively; a naive implementation will make n calls on the input n. We can speed things up by trading space for time: we'll use a dictionary to remember the result. Here's a manual implementation:

.. runner::

    fact_cache = dict()
    def factorial(n):
        global fact_cache
        
        # look for the result in the cache
        if n in fact_cache:
            # cache hit! just return the saved answer
            return fact_cache[n]

        print(f'actually doing factorial({n})')
        # cache miss :( compute the answer
        assert isinstance(n, int)
        assert n >= 0

        if n < 2: return 1

        # calculate result
        res = n * factorial(n-1)
        # store it in the cache
        fact_cache[n] = res

        return res

    print(factorial(5))
    print(factorial(10))
    print(factorial(6))

Notice how few calls got made... nice! It was a lot of work, though, and now we have this awkward global ``fact_cache`` lying around.

It turns out, Python can do the caching for you *automatically*. Check it out:

We get the same output, and we didn't have to create or manage our cache. Nice! There are other useful decorators in `the functools package <https://docs.python.org/3/library/functools.html>`_, but you'll find other useful decorators in all kinds of places.