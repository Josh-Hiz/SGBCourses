Unbounded repetition
====================

It's not uncommon to want to match some unbounded repetition. For example, suppose we had a text file containing the text of a book, and we wanted to get all of the words out of it---ignoring punctuation or numbers. What is a word? We might say it's a sequence of one-or-more letters, with no upper bound.

Alternatively, suppose we wanted to find all of the numbers in a file that mixed text and numbers. We might look for one-or-more numbers, ignoring the rest.

Finally, we might want to allow an arbitrary amount of whitespace between things (e.g., a credit card number is 4 groups of four, and the spaces don't matter). We might want to match here against zero-or-more whitespace characters.

All three of these examples rely on **unbounded repetition**. We can express unbounded repetition using curly braces by just leaving the upper number off:

.. runner:: 

    import re

    print(re.findall(r"[a-zA-Z]{1,}",'these are the words for h4x0rs'))

The ``{1,}`` means one-or-more iterations of ``[a-zA-Z]``, i.e., Latin letters. The ``...{1,}`` pattern is so common, that it can be written directly as ``...+``:

.. runner:: 

    import re

    print(re.findall(r"[a-zA-Z]+",'these are the words for h4x0rs'))


Similarly, the zero-or-more pattern can be written as ``...*``; this operator is called `Kleene star <https://en.wikipedia.org/wiki/Kleene_star>`_, named after Stephen Cole Kleene. (The ``...+`` is sometimes called Kleene plus.)

For example, here's a regular expression that matches many floating point numbers:

.. runner:: 

    import re

    print(re.findall(r"-?(?:\d*\.\d+|\d+)",'1 -1 2 -2 1.3 -1.3 -0.3333 -.5 .5'))

There's a lot going on here! Let's piece it apart:

* Optional negative up front
* An overall non-capturing group, with two alternatives
    * \d*\.\d+ is zero-or-more digits, a decimal point, and one or more digits
    * \d+ is just one or more digits