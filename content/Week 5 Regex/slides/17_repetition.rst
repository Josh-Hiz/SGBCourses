Repetition
==========

Regular expressions show their power when we want to handle repetition. We'll start by looking at finite repetition, and work our way up to unbounded repetition.

Suppose we wanted to represent a decimal number with up to three places before and after the decimal. We might write something like:

.. runner:: 

    import re

    r = r"(\d\d\d|\d\d|\d)\.(\d\d\d|\d\d|\d)"
    print(re.findall(r, "1.0 100.23 999.999 0.001"))

A little wordy, but it works.


There's a nicer syntax for this kind of bounded repetition: ``...{m,n}``, when ``m <= n``, means between ``m`` and ``n`` repetitions. So we could instead say:

.. runner:: 

    import re

    r = r"(\d{1,3})\.(\d{1,3})"
    print(re.findall(r, "1.0 100.23 999.999 0.001"))

The repetition applies to whatever came before it. Here, that's ``\d``. If you want it to repeat something longer, using a group is a good idea:

.. runner:: 

    import re

    r = r"b(?:an){2,10}a"
    print(re.findall(r, "b ban banan banana bananana banananananananana"))

Idioms and shorthands
---------------------

There are several common idioms with ``{m,n}`` that get shorthands.

Exact repetitions with ``...{m}``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We might also want an exact number of repetitions. Rather than writing ``...{m,m}``, we can simply write ``...{m}``, as in:

.. runner:: 

    import re

    r = r"b(?:an){2}a"
    print(re.findall(r, "b ban banan banana bananana banananananananana"))

Zero or one repetitions with ``?``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If something is optional, it occurs 0 or 1 times. Instead of writing ``...{0,1}``, you can write ``...?``.

.. runner:: 

    import re

    r = r"b(?:an){2}a?"
    print(re.findall(r, "b ban banan banana bananana banananananananana"))


