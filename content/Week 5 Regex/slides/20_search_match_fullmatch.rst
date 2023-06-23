Using re.search, re.match, and re.fullmatch
===========================================

So far we've used ``re.findall``; ``re.search``, ``re.match``, and ``re.fullmatch`` are three other important functions in the ``re`` module.

All three of ``re.search``, ``re.match``, and ``re.fullmatch`` find a *single* match of a regular expression in a string. All three return a ``Match`` object, or ``None`` if the pattern doesn't match. The function ``re.search`` will search the whole string, but ``re.match`` and ``re.fullmatch`` both start at the beginning of the string. The only difference between these last two is that the ``re.fullmatch`` function tries to match the *whole* string while ``re.match`` is okay with some leftover. Let's play with it!

.. runner:: 

    import re

    identifier = r"\s*([a-zA-z_]\w*)\s*"
    print('re.search')
    print(re.search(identifier, "this_is_a_valid_python_identifier"))
    print(re.search(identifier, "\n\tthis_is_a_valid_python_identifier  "))
    print(re.search(identifier, "this_is_a_valid_python_identifier and_so_is_this"))
    print(re.search(identifier, "999 this_is_a_valid_python_identifier and_so_is_this"))

    print('\nre.match')
    print(re.match(identifier, "this_is_a_valid_python_identifier"))
    print(re.match(identifier, "\n\tthis_is_a_valid_python_identifier  "))
    print(re.match(identifier, "this_is_a_valid_python_identifier and_so_is_this"))
    print(re.match(identifier, "999 this_is_a_valid_python_identifier and_so_is_this"))

    print('\nre.fullmatch')
    print(re.fullmatch(identifier, "this_is_a_valid_python_identifier"))
    print(re.fullmatch(identifier, "\n\tthis_is_a_valid_python_identifier  "))
    print(re.fullmatch(identifier, "this_is_a_valid_python_identifier and_so_is_this"))
    print(re.fullmatch(identifier, "999 this_is_a_valid_python_identifier and_so_is_this"))

Notice how the two behave the same when whole string matches, but ``fullmatch`` returns ``None`` when there's more text after the space---because the *whole* string didn't match.

Match objects
-------------

Both ``re.match`` and ``re.fullmatch`` return a ``Match`` object. The ``Match.__str__`` method gives you some basic information about what the ``Match`` object holds: the ``span`` tells you the indices of the string that matched; the ``match`` tells you the part of the string that matched. You can get this information out using some methods, used in our ``show_match`` helper:

.. runner:: 

    import re

    def show_match(m):
        if m is None:
            print('no match')
            return

        span = m.span()

        # two different ways to get the same value
        assert m.string[span[0]:span[1]] == m.group(0)
        print(f'matched characters {span[0]} through {span[1]}: "{m.group(0)}"')
        print(f'  the captured group was "{m.group(1)}"')

    identifier = r"\s*([a-zA-z_]\w*)\s*"
    print('re.search')
    show_match(re.search(identifier, "this_is_a_valid_python_identifier"))
    show_match(re.search(identifier, "\n\tthis_is_a_valid_python_identifier  "))
    show_match(re.search(identifier, "this_is_a_valid_python_identifier and_so_is_this"))
    show_match(re.search(identifier, "999 this_is_a_valid_python_identifier and_so_is_this"))

    print('\nre.match')
    show_match(re.match(identifier, "this_is_a_valid_python_identifier"))
    show_match(re.match(identifier, "\n\tthis_is_a_valid_python_identifier  "))
    show_match(re.match(identifier, "this_is_a_valid_python_identifier and_so_is_this"))
    show_match(re.match(identifier, "999 this_is_a_valid_python_identifier and_so_is_this"))

    print('\nre.fullmatch')
    show_match(re.fullmatch(identifier, "this_is_a_valid_python_identifier"))
    show_match(re.fullmatch(identifier, "\n\tthis_is_a_valid_python_identifier  "))
    show_match(re.fullmatch(identifier, "this_is_a_valid_python_identifier and_so_is_this"))
    show_match(re.fullmatch(identifier, "999 this_is_a_valid_python_identifier and_so_is_this"))

The ``m.span()`` method gets you the span of the string that matched: i.e., a tuple with the start and end indices of the match. The ``m.group()`` method is more interesting: takes a non-negative integer as its argument. The group 0 is the whole part of the string that matched; the group 1 is the first capturing group (from the left of the regex) that matched; group 2 is the second, and so on. Note that ``m.group(1)`` extracts the capturing group of the "identifier" part itself, ignoring the space.

The conditional in ``show_match``---here testing for ``None`` and returning early---is a common idiom in regex processing in Python. It is perhaps more common to see if ``m: ...``, though here it's more concise to test the other way.