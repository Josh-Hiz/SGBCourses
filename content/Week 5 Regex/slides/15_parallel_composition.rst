Choice a/k/a parallel composition; groups
=========================================

Regular expressions let us offer **choice** using the ``|`` symbol, which is called **parallel composition** or simply **or**, i.e., disjunction.

For example, we can recognize common `TLDs <https://en.wikipedia.org/wiki/Top-level_domain>`_ using a regular expression as follows:

.. runner:: 

    import re

    tld = r"com|edu|net|org"
    print(re.findall(tld, "google.com stevens.edu"))

If we wanted to match the dot as well, we might write:

.. runner:: 

    import re

    tld = r"\.com|\.edu|\.net|\.org"
    print(re.findall(tld, "google.com stevens.edu bonnet korg"))

You may feel like writing the ``\.`` each time is too much. We can simplify things by saying "first match a literal ``.``, then match the TLD". To express that logic, we need **groups**. A group in a regular expression is expressed using parentheses ``(`` and ``)``.

.. runner:: 

    import re

    tld = r"\.(com|edu|net|org)"
    print(re.findall(tld, "google.com stevens.edu bonnet korg"))

You can arbitrarily nest groups and choices. But: notice what ``findall`` does:

Why is ``findall`` returning tuples? Groups, by default, are **capturing**, i.e., they indicate that some part of the regular expression is interesting and should be held on to. Python's ``re`` module keeps track of every captured group, and ``re.findall`` will return it. Let's piece the output apart:

.. code-block:: 

    >>> re.findall(r"(a|(b(c|de)))", "a bc bde")
    [('a', '', ''), ('bc', 'bc', 'c'), ('bde', 'bde', 'de')]

If we look at our regex ``r"(a|(b(c|de)))"``, there are three groups, from the outside in:

1. ``(a|...)`` is the outermost
2. ``(b(...))`` is the middle
3. ``(c|de)`` is the innermost

The 3-tuple returned by ``findall`` contains the matches for these groups, in that order.

The first match ``('a', '', '')`` says that "a" matched the outermost group, ``(a|...)``, but the two inner groups didn't match anything.

The second match ``('bc', 'bc, 'c')`` says that the outermost group matches on "bc", as did the middle one; the innermost group only matched on "c".

The capturing aspect of groups can be confusing, especially if you just want all the matches. By default, if there are *any* capturing groups, that will be *all* that ``findall`` returns. Look at what happens if we remove the outermost capturing group:

.. runner:: 

    import re

    tld = r"a|(b(c|de))"
    print(re.findall(tld, "a bc bde"))

Since the outermost group is gone, the match on "a" has lost all of its information! Not so good. The solution here is to use a non-capturing group, written ``(?:...)``.

.. runner:: 

    import re

    tld = r"a|(?:b(?:c|de))"
    print(re.findall(tld, "a bc bde"))

Ah: now it's just giving us the matching parts back.

The longest match
-----------------

In general, ``re`` will always try to find you the longest possible match. Choice with ``|`` can mess that up, because it takes an eager approach: if the left-hand side of ``|`` matches, ``re`` will never look at the right-hand side. So you might expect the following to return ``('999', '999')``... but it doesn't!

.. runner:: 

    import re

    print(re.findall(r"(\d|\d\d|\d\d\d)\.(\d|\d\d|\d\d\d)", '999.999'))

Why do we get ``('999', '9')``? When exploring the first group, ``re.findall`` has to match all three digits before the decimal mark to continue. But after that, the first ``\d`` matches just fine---and we'll ignore the last two ``9``'s in the input!

To avoid this confusing behavior, think carefully about the order of your choices: if they overlap, you want to put the longer/preferable one first.