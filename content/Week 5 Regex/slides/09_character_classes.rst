Characters and character classes
================================

We'll explain regular expressions by giving regular expressions and examples of what they match against; we'll learn about extracting information from matches and doing substitutions once we've mastered the basics.

Matching
--------

We say a regular expression matches a string if some part of the string is exactly described by the regular expression. (Later on, we'll learn how to say 'the whole string'.)

By default, every character in regular expression matches itself. So the regular expression ``aa`` matches three 'a's in a row; it matches the beginning of ``aardvark``, but not ``AAPL``---because case matters! It also matches ``baa baa black sheep`` in two places.

Matching any character (except a newline): ``.``
------------------------------------------------

Some characters, however, are special. The ``.`` character means "any character" (except a newline). So the regular expression matches ``a.`` matches ``aardvark`` twice: once for ``aa`` and once for ``ar``; the regular expression ``a.`` *doesn't* match ``la``, because no character comes after the ``a``; it matches ``la la la`` twice: the first `a`  and the second ``a`` ... recall that space is a character, and ``.`` matches *any* character.

Matching any of a selection of characters: ``[]``
-------------------------------------------------

Sometimes you want to allow any of a few possible characters. Square brackets are used to indicate a **character class**.

For example, the regular expression ``[ab]cd`` matches ``acd`` and ``bcd`` exactly. The regular expression ``i[sz]e`` matches the last three characters of ``specialise`` and ``specialize``. The character class ``[0123456789]`` matches digits, i.e., it matches ``0`` or ``1`` but not ``e``.

Note that the order here doesn't really matter: ``[ab]`` is the same as ``[ba]``. Since it's a set of characters, repeats are innocuous, i.e., they have no effect: ``[abba]`` is the same as ``[aba]`` is the same as ``[ab]``.

Matching everything but a selection of characters: ``[^]``
----------------------------------------------------------

Sometimes you want to *disallow* any of a few possible characters. Putting a caret mark (^) at the beginning of brackets makes it a **negated character class**, i.e., it matches all characters except those named.

For example, the regular expression ``tot[^e]`` matches ``total`` and ``tottering``, not ``totem``. The regular expression ``[^0123456789]`` matches non-digits, i.e., it matches ``a`` or ``*`` or ``(`` but not ``6`` or ``7``.

Large, common groups: ranges and predefined character classes
-------------------------------------------------------------

Character classes are very useful, but sometimes you want to match a very large set of possibilities, e.g., every letter, or every whitespace character. Two features help you here: ranges and predefined character classes.

Ranges are written as, e.g., ``[a-z]`` to represent any lowercase character in the range ``a`` through ``z``. As readers and writers of English, we know that ``[a-z]`` should be the same as ``[abcdefghijklmnopqrstuvwxyz]``. But you should be careful with obscure ranges. For example what does the range ``[0-A]`` mean? By default, a modern Python will be using `UTF-8 <https://en.wikipedia.org/wiki/UTF-8>`_ (i.e., Unicode with an 8-byte character size by default) which coincides with `ASCII <https://en.wikipedia.org/wiki/ASCII>`_ on the first 127 code points; if you write out `a table <https://www.unicode.org/charts/PDF/U0000.pdf>`_, you'll see that ``[0-A]`` corresponds to ``[0123456789:;<=>?@A]``... an odd grouping! Worse still, other character encodings for Python could give you different ranges. It's best to only write ranges within natural sequences, e.g., ``[a-zA-Z]`` matches against any one Latin character, lower or uppercase; ``[a-zA-Z0-9]`` matches any Latin character or digit.

To avoid confusion, it's best to use predefined character classes when possible. They are generally of the form ``\x`` to mean "has quality ``x``" and ``\X`` to mean "does not have quality ``x``".

* ``\d`` matches digits---not just 0 through 9, but also Devanagari digits like १. Han/Suzhou digits are not included here, according to the `Unicode Consortium <https://www.unicode.org/terminology/digits.html>`_.
* ``\w`` matches 'word characters', namely letters, digits, and underscores. This includes not just Latin letters and western Arabic numerals (0-9), but also other digits, letter characters, and ideograms. Every character in ``abc_५६७123é四공`` matches ``\w``, and none of them match ``\W`` (non-word characters).
* ``\s`` matches whitespace characters---not just  , but also tabs and newlines and carriage returns... and even more obscure whitespace! ``\S`` matches non-whitespace.

