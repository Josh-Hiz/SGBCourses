Filtering and Mapping
=====================

Filtering
---------

Oftentimes, we have a list of elements and we want to select only a few from it. A common task in a music application, for example, is to select just the songs by a particular artist or from a particular genre. Python (along with many other programming languages) has a function for doing this with lists called ``filter``.

Using filter requires that we first write a function that **checks** for the items we want from the list. As a first example, let's try to filter a list of numbers to get just the elements that are less than 10. We need a function that checks numbers to see their size:

.. code-block:: 

    >>> def less_than_10(n): return n < 10

Then we can use this function with filter on a list:

.. code-block:: 

    >>> l = [5, 100, 3, 50, 6]
    >>> list(filter(less_than_10, l))
    [5, 3, 6]

Here's what happened:

* filter went one-by-one through the elements of the list, and for each: 

    * Called the less_than_10 function with that element

    * If the result was True, put the element in the collection it eventually returned

    * If the result was False, left the element out of the collection it eventually returned

The use of ``list(...)`` tells Python that we want to get the resulting collection back as a list (there are other kinds in Python, but we aren't using them right now).

(Above, we defined a function all on one line – this is allowed in Python and is a reasonable thing to do for short functions whose body is just a simple expression. If the body has an if-statement or other multi-line statement, or would be wider than about half a screen-width (this is a bit subjective), it shouldn't be a one-line function.)

Here's another example that keeps only the strings that are longer than 5 characters:

.. code-block:: 

    >>> def long_string(s): return len(s) > 5
    ...
    >>> l2 = ["long string", "short", "small", "longer"]
    >>> list(filter(long_string, l2))
    ['long string', 'longer']


So filter takes two arguments - a function and a list. It expects the function to take **one argument**, which will get elements from the list and return ``True`` or ``False``. Such functions are often called **predicates**, a word you may have heard in math. It then calls that function on each element, and produces a new collection of just the elements for which that function returns ``True``.

Mapping
-------

Another common operation on lists is to make a new list with elements based on the existing ones somehow. For example, we might want to take a list of all the students in a class and get a list of all of their email addresses, or take a list of names and turn them into a list of form emails with the names filled in. Python (along with many other programming languages) has a function for doing this called ``map``.

Using ``map`` requires we first write a function that **transforms** the elements into the new kind of elements. As a first example, let's try to map a list of numbers to those numbers squared. We need a function that squares numbers:

.. code-block:: 

    >>> def square(x): return x * x
    ...
    >>> l = [4, 3, 7, 6]
    >>> list(map(square, l))
    [16, 9, 49, 36]

Here's what happened:

* ``map`` went one-by-one through the elements of the list, and for each: 

    * Called the ``square`` function with that element

    * Put the resulting value into the collection it eventually returned 

Here's another example that makes all the strings all capitals with exclamation points:

.. code-block:: 

    >>> def shout(s): return s + "!"
    ...
    >>> l = ["MAP", "IS", "SO", "COOL"]
    >>> list(map(shout, l))
    ['MAP!', 'IS!', 'SO!', 'COOL!']