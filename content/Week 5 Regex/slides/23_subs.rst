Substitutions and backreference
===============================

Regular expressions not only express matching, but they're also useful for expressing substitutions and replacements. The function ``re.sub`` helps you do such a substitution. Here's the help text:

**sub(pattern, repl, string, count=0, flags=0)**

    Return the string obtained by replacing the leftmost non-overlapping occurrences of the pattern in string by the replacement repl.  repl can be either a string or a callable; if a string, backslash escapes in it are processed.  If it is a callable, it's passed the Match object and must return a replacement string to be used.

Here's an example of how to use it:

.. runner:: 

    import re

    print(re.sub("(\w+)\s+(\w+)", r"\2, \1", "Michael Greenberg"))

What's happening here? The first argument to ``re.sub`` is the pattern to match in the string. The second argument is the *replacement*, i.e., what do with the parts of the string that match. The third argument is the string to work on. The net effect is to transform ``"Michael Greenberg"`` into ``"Greenberg, Michael"``. Neat! But what are ``\1`` and ``\2``?

The form ``\N`` where ``N`` is a number is a **backreference**. Used primarily for substitutions, backreferences refer to the group numbers from ``match.group``. So ``\1`` refers to the first group of one-or-more word characters (here, ``"Michael"``) and ``\2`` refers to the second group of one-or-more word characters (here, ``"Greenberg"``). The rest of the replacement is fixed---you can think of it as a string with a few of these backreferences thrown in.

Backreference is pretty powerful: you can do quite a bit with very little. For example:

.. runner:: 

    import re

    print(re.sub("(\w+),\s+((\w+)(?:\s+\w+)*)",
                r"\2 \1. But you can call me \3.",
                "Greenberg, Michael Matthew"))

Even if you have capturing groups, you have no obligation to use those groups.

.. runner:: 

    import re

    print(re.sub("(\w+),\s+((\w+)(?:\s+\w+)*)",
                r"My first name is \3.",
                "Greenberg, Michael Matthew"))