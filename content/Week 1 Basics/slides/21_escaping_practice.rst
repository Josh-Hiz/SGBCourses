Escaping Practice
=================

.. quizdown::

    ## Which definitions of s will Python accept?

    - [x] ```s = "don't"```
    - [ ] ```s = "don"t"```
    - [x] ```s = "don\'t"```
    - [x] ```s = 'don\'t'```
    - [ ] ```'don't'```

.. free-r::
    :answer: "hello\\n world\\n  how are you\?"|'hello\\n world\\n  how are you\?'
    :regex: true

    # Question 2

    How would you write the following as a string in Python?

    ```python
    hello
     world
      how are you?
    ```

    Just write the string literal, as in ```"this\tis not  the answer"```.

    >>>Correct answer must match the regular expression ("hello\\n world\\n how are you\?"|'hello\\n world\\n how are you\?')

.. free-r::
    :answer: '"It\\'s a backslash," he said, "you write it like \\'\\\\\\'\."'|"\\"It\\?'s a backslash,\\" he said, \\"you write it like \\?'\\\\\\?'\.\\""
    :regex: true

    # Question 3

    How would you write the following as a string in Python?

    ```"It's a backslash," he said, "you write it like '\'."```

    Just write the string literal, as in ```"this\tis not  the answer"```.

    >>>
    ```'"It\'s a backslash," he said, "you write it like \'\\\'."'```<br>
    or<br>
    ```"\"It's a backslash,\" he said, \"you write it like '\\'.\""```