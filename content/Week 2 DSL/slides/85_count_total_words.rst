count_total_words
=================

Given a dictionary ``word_freq`` that maps a word to the frequency count (i.e., number of times the word occurs in a sentence), write a function ``count_total_words`` to return the total number of words in the sentence.

For example, if the sentence is "all is well that ends well", then the dictionary will contain ``{"all":1, "is":1, "well":2, "that":1, "ends":1}``. Your function should count the total number of words in that dictionary (including duplicates). For this example, your function should return 6.

Another example: if the sentence is "I scream you scream we all scream for ice cream", the ``word_freq`` dictionary (i.e., input parameter to the function) will contain ``{"I":1, "scream":3, "you":1, "we":1, "all":1, "for":1, "ice":1, "cream":1}`` and your function should return 10.

**Sample Input 1:**

.. code-block::

    {"all":1, "is":1, "well":2, "that":1, "ends":1}

**Sample Output 1:**

.. code-block:: 

    6

**Sample Input 2:**

.. code-block::

    {"I":1, "scream":3, "you":1, "we":1, "all":1, "for":1, "ice":1, "cream":1}

**Sample Output 2:**

.. code-block:: 

    10

.. challenge::

    # a helper for testing
    def is_letter(c): return c.isalpha()
    def to_letters(s): return ''.join(filter(is_letter, s))

    def word_frequency(sentence):
        words = list(map(to_letters, sentence.lower().split()))
        word_freq = {}
        for word in words:
            count = word_freq.get(word, 0)
            word_freq[word] = count + 1

        return word_freq

    assert word_frequency("all is well that ends well") == {"all":1, "is":1, "well":2, "that":1, "ends":1}
    assert word_frequency("I scream, you scream, we all scream for ice cream!") == {"i":1, "scream":3, "you":1, "we":1, "all":1, "for":1, "ice":1, "cream":1}

    # define count_words(word_freq)

    # here are some tests
    assert count_words(word_frequency("all is well that ends well")), 6
    assert count_words(word_frequency("I scream, you scream, we all scream for ice cream!")) == 10