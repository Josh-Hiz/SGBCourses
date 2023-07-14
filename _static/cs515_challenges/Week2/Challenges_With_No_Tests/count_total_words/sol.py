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
def count_words(word_freq):
    return sum([item for item in word_freq.values()])

# here are some tests
assert count_words(word_frequency("all is well that ends well")), 6
assert count_words(word_frequency("I scream, you scream, we all scream for ice cream!")) == 10