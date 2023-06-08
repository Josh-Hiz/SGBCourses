Part 3: A Datatype for Text
===========================

So far, all the functions and operators we've worked with have been only numbers. There are many more kinds of data in the world than numbers and we'll want to represent those in our programs as well. One common kind of data is text. This lesson is stored as text that your browser loads for you to read. In the university's registration system, your name is stored as text. Emails and email addresses, song and artist names in a music player, the words in an e-book, and more are all stored and manipulated in computers as text.

In Python (and many other programming languages) we can create text data by writing some characters in between single or double quotes:

.. code-block:: python

        >>> "CS 515-A"
        'CS 515-A'
        >>> 'CS 515-A'
        'CS 515-A'

We can put almost any characters between the quotes, including spaces.

.. code-block:: python

        >>> "this is a sentence"
        'this is a sentence'

We call these **strings** and they are a datatype for storing text. So we've seen two **types** of data so far: **integers** and **strings**.

Notice that just like with numbers, Python prints out string values when they are the answer to an expression we type in.

Concatenation
-------------

Strings work with some operators. For example, they work with +:

.. code-block:: python

        >>> "this is a " + "sentence"
        'this is a sentence'

The result of this + expression is the combined string. We often refer to this operation as **concatenating** or **appending** strings.

Replication
-----------

A string can be replicated multiple times using the * operator.

.. code-block:: python

        >>> 'ha' * 10
        'hahahahahahahahahaha'

The result of above expression is the string 'ha' repeated 10 times. We often refer to this operation as **replicating** strings.

Escapes
-------

What if you want a quote in a string? If you're using double quotes for the string, then you can use single quotes freely:

.. code-block:: python

        >>> "it's me"
        "it's me"

And likewise for double quotes inside of single quotes:

.. code-block:: python

        >>> '"Hi," he said.'
        '"Hi," he said.'

But what if you want to have both? Then you need an *escape*. In programming you escape a character to turn off its special meaning. The most common character for escapes is what Python uses: backslash, ``\``. 

.. code-block:: python

        >>> '"It\'s me," he said, "I\'m the one you\'re looking for."'
        '"It\'s me," he said, "I\'m the one you\'re looking for."'
        >>> "\"It's me,\", he said, \"I'm the one you're looking for.\""
        '"It\'s me,", he said, "I\'m the one you\'re looking for."'

As an experiment, try entering the string ``"It's me,", he said, "I'm the one you're looking for."`` without any escapes... what does Python say?

