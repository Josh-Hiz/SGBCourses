Part 1: The Basics of Numbers and Variables
===========================================

Programs do their work with data. Some of the data is text (like a person's name), some is pretty sophisticated (like a file containing audio or video), some of it is yes/no (like whether a box is checked) and quite a bit of it is *numbers*.

Numbers are a convenient place to start studying programs, because we have some familiarity with them already, and at least at first, Python won't violate our understanding of how numbers work and some our experience will help us.

At a Python prompt (at a terminal running ``python`` in a Workspace), try typing a number and pressing enter. Here's what you should expect to see:
HELLO

.. code-block:: 

        [user@sahara ~]$ python
        Python 3.9.6 (default, Jun 30 2021, 10:22:16) 
        [GCC 11.1.0] on linux
        Type "help", "copyright", "credits" or "license" for more information.
        >>> 4
        4
        
(We'll skip the noise and just show ``>>>`` from now on.) We typed in a number, and Python printed it back out at us. Let's try with arithmetic:

.. code-block:: python

        >>> 4 + 3
        7
        >>> 4 + 3 + 9
        16

We're showing one of the most familiar tasks we can accomplish with Python – we can use it as a calculator! Python is equipped with many familiar arithmetic operations, like \*, /, +, and -. It also evaluates operations in parentheses first, like we may expect from math:

.. code-block:: python
        
        >>> 4 * 8 - 2
        30
        >>> 4 * (8 - 2)
        24

We can *nest* the parentheses and expressions as much as we like, and Python will calculate the answer for us:

.. code-block:: python
        
        >>> 4 * (8 - 2) + 3 * (99 / (2 + 1))
        123

So Python is a pretty good calculator! Crucially, we're seeing here a fundamental kind of behavior of how programming languages work. We write *programs*, which are text, and Python *evaluates* them, producing values (in this case, the values are numbers).

Importantly, Python (and most programming languages) won't give back an answer that's an unevaluated or partially evaluated expression like ``3 * 7``. Instead, each expression is fully evaluated to a value, and then the result is used.