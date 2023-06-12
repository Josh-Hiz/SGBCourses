Dots and dashes
===============

There are ``split`` and ``join`` string methods as well (see Week 3!). Write a function called ``chain_words(str)`` which takes in one parameter which is a string that holds multiple words separated by spaces. Your function should return a string with the words chained together with an - (hyphen). You can first split the words at spaces and then join the words with - (hyphen). You can achieve this by using split and join methods respectively.

**Sample Input 1:**

.. code-block:: 

    hello world

**Sample Output 1:**

.. code-block:: 

    hello-world

**Sample Input 2:**

.. code-block:: 

    Connect the words in this sentence

**Sample Output 2:**

.. code-block:: 

    Connect-the-words-in-this-sentence

.. challenge:: 
    :tester: /_static/cs515_challenges/Week2/Challenge10/test_task.py

    # define chain_words