Tries
=====

A `trie <https://en.wikipedia.org/wiki/Trie>`_ is a special kind of tree-shaped data structure. We'll meet more such data structures soon, but we'll be using tries here to represent a set of words.

The gist of a trie is that it represents words by their prefixes, which makes it very easy and efficient to lookup, insert, and remove words from the set.

You'll implement three operations: ``trie_insert``, ``trie_lookup``, and ``trie_delete``. First, let's understand what a trie is.

Suppose we wanted to represent a set of five words: he, hey, hem, his, and we. Our trie will model them pictorially as:

.. image:: /assets/images/cs515/RecursionWorkbook/image.png

Each letter represents a part of the trie; a 👍 sign means that the path from the root to that letter is a word in the trie. (Notice that 'hi' is a real word, but it's not recorded as such in our trie.) As a Python data structure, we have:

.. code-block:: 

    t = {'h': {'e': {'is_word': True, 
                    'y': {'is_word': True}, 
                    'm': {'is_word': True}}, 
             'i': {'s': {'is_word': True}}},
       'w': {'e': {'is_word': True}}}


That is, a trie is a series of nested dictionaries, where each key is a letter or ``'is_word'``. At a given level, ``is_word`` means that the path from the root to that point is a word, i.e., ``'he'`` is a word because ``t['h']['e']['is_word']`` is ``True``. We don't bother recording ``'is_word'`` as ``False``, since it would make the output noisy.

Notice that every key in the outer dictionary of a trie is either ``'is_word'`` or a letter; if it's ``'is_word'``, it maps to a boolean. If it's a letter, it maps to... another trie! We call this other trie the *child* and the outer one is the *parent*.

For all of the following functions, both recursion and loops work. It's up to you which you use!

Adding a word to a trie with ``trie_insert``
--------------------------------------------

Let's get a feel for tries by writing ``trie_insert``. The function should take a string ``word`` and a trie ``t``; it should update ``t`` so that the path to ``word`` is in ``t`` and ``'is_word'`` is set.

Here are some examples:

.. code-block:: 

    >>> t = {}
    >>> trie_insert('hem', t)
    >>> t
    {'h': {'e': {'m': {'is_word': True}}}}
    >>> trie_insert('hey', t)
    >>> t
    {'h': {'e': {'m': {'is_word': True}, 'y': {'is_word': True}}}}
    >>> trie_insert('he', t)
    >>> t
    {'h': {'e': {'m': {'is_word': True}, 'y': {'is_word': True}, 'is_word': True}}}
    >>> trie_insert('we', t)
    >>> t
    {'h': {'e': {'m': {'is_word': True}, 'y': {'is_word': True}, 'is_word': True}}, 'w': {'e': {'is_word': True}}}

Write four asserts as tests; don't just copy what we have here.

Looking words up in the trie with ``trie_lookup`` 
-------------------------------------------------

Now that we can build tries, lets write a function to see whether a given word is in a trie. Write the function ``trie_lookup``, which takes a string ``word`` and trie ``t``, returning ``True`` if the ``word`` is in the trie (i.e., the path to it exists and ``is_word`` is present and ``True``).

Here are some examples:

.. code-block:: 

    >>> t
    {'h': {'e': {'is_word': True, 'm': {'is_word': True}, 'y': {'is_word': True}}, 'i': {'s': {'is_word': True}}}, 'w': {'e': {'is_word': True}}}
    >>> trie_lookup('he', t)
    True
    >>> trie_lookup('head', t)
    False
    >>> trie_lookup('wed', t)
    False
    >>> trie_lookup('we', t)
    True
    >>> trie_lookup('', t)
    False

Write four asserts as tests; don't just copy what we have here.

Removing words from the trie with ``trie_remove`` 
-------------------------------------------------

You might notice that ``trie_remove`` above leaves some empty dictionaries lying around. How unsightly! As a **completely optional** challenge problem, write a new function ``trie_remove_cleanup`` that makes sure these empty dictionaries are cleared out. (This function is a bit easier to write using recursion than loops---with loops, it's harder to cleanup without re-traversing the trie again.)

Here are some examples---though this isn't for credit and won't be graded.

.. code-block:: 

    >>> t
    {'h': {'e': {'is_word': True, 'm': {'is_word': True}, 'y': {'is_word': True}}, 'i': {'s': {'is_word': True}}}, 'w': {'e': {'is_word': True}}}
    >>> trie_remove_cleanup('hey', t)
    >>> t
    {'h': {'e': {'is_word': True, 'm': {'is_word': True}}, 'i': {'s': {'is_word': True}}}, 'w': {'e': {'is_word': True}}}
    >>> trie_remove_cleanup('hem', t)
    >>> t
    {'h': {'e': {'is_word': True}, 'i': {'s': {'is_word': True}}}, 'w': {'e': {'is_word': True}}}
    >>> trie_remove_cleanup('his', t)
    >>> t
    {'h': {'e': {'is_word': True}}, 'w': {'e': {'is_word': True}}}
    >>> trie_remove_cleanup('he', t)
    >>> t
    {'w': {'e': {'is_word': True}}}
    >>> trie_remove_cleanup('we', t)
    >>> t
    {}

.. challenge:: 
    :tester: /_static/cs515_challenges/Workbook/Challenge2/test_task.py


    # define trie_insert
    # write 4 asserts (outside of the function)

    # then define trie_lookup
    # write 4 asserts (outside of the function)

    # then define trie_remove
    # write 4 asserts (outside of the function)

