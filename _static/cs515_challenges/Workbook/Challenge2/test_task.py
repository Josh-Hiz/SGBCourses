import challenge as task
import unittest

def build(words):
    t = {}
    for word in words:
        task.trie_insert(word, t)
    return t

def lookup(word, d):
    for c in word:
        if c not in d:
            return False
        d = d[c]

    return d.get('is_word', False)

class TestTrie(unittest.TestCase):
    def test_insert1(self):
        t = build(['hem'])
        self.assertEqual(lookup('hem', t), True)
        self.assertEqual(lookup('he', t), False)
        self.assertEqual(lookup('h', t), False)
        self.assertEqual(lookup('hey', t), False)

    def test_insert2(self):
        t = build(['hem', 'hey'])
        self.assertEqual(lookup('hem', t), True)
        self.assertEqual(lookup('he', t), False)
        self.assertEqual(lookup('h', t), False)
        self.assertEqual(lookup('hey', t), True)
        self.assertEqual(lookup('yeh', t), False)
    
    def test_insert3(self):
        t = build(['hem', 'hey', 'he'])
        self.assertEqual(lookup('hem', t), True)
        self.assertEqual(lookup('he', t), True)
        self.assertEqual(lookup('h', t), False)
        self.assertEqual(lookup('hey', t), True)
        self.assertEqual(lookup('yeh', t), False)

        t = build(['he', 'hey', 'hem'])
        self.assertEqual(lookup('hem', t), True)
        self.assertEqual(lookup('he', t), True)
        self.assertEqual(lookup('h', t), False)
        self.assertEqual(lookup('hey', t), True)
        self.assertEqual(lookup('yeh', t), False)

    def test_insert4(self):
        t = build(['hem', 'hey', 'he', 'he', 'hey', 'hem'])
        self.assertEqual(lookup('hem', t), True)
        self.assertEqual(lookup('he', t), True)
        self.assertEqual(lookup('h', t), False)
        self.assertEqual(lookup('hey', t), True)
        self.assertEqual(lookup('yeh', t), False)

        t = build(['he', 'hey', 'hem', 'he', 'hey', 'hem'])
        self.assertEqual(lookup('hem', t), True)
        self.assertEqual(lookup('he', t), True)
        self.assertEqual(lookup('h', t), False)
        self.assertEqual(lookup('hey', t), True)
        self.assertEqual(lookup('yeh', t), False)

    def test_lookup_empty(self):
        t = {}
        self.assertEqual(lookup('hi', t), False)
        self.assertEqual(lookup('', t), False)
        self.assertEqual(lookup('hello', t), False)
        self.assertEqual(lookup(' ', t), False)
    def test_lookup1(self):
        t = build(['hem'])
        self.assertEqual(task.trie_lookup('hem', t), True)
        self.assertEqual(task.trie_lookup('he', t), False)
        self.assertEqual(task.trie_lookup('h', t), False)
        self.assertEqual(task.trie_lookup('hey', t), False)

    def test_lookup2(self):
        t = build(['hem', 'hey'])
        self.assertEqual(task.trie_lookup('hem', t), True)
        self.assertEqual(task.trie_lookup('he', t), False)
        self.assertEqual(task.trie_lookup('h', t), False)
        self.assertEqual(task.trie_lookup('hey', t), True)
        self.assertEqual(task.trie_lookup('yeh', t), False)
    
    def test_lookup3(self):
        t = build(['hem', 'hey', 'he'])
        self.assertEqual(task.trie_lookup('hem', t), True)
        self.assertEqual(task.trie_lookup('he', t), True)
        self.assertEqual(task.trie_lookup('h', t), False)
        self.assertEqual(task.trie_lookup('hey', t), True)
        self.assertEqual(task.trie_lookup('yeh', t), False)

        t = build(['he', 'hey', 'hem'])
        self.assertEqual(task.trie_lookup('hem', t), True)
        self.assertEqual(task.trie_lookup('he', t), True)
        self.assertEqual(task.trie_lookup('h', t), False)
        self.assertEqual(task.trie_lookup('hey', t), True)
        self.assertEqual(task.trie_lookup('yeh', t), False)

    def test_lookup4(self):
        t = build(['hem', 'hey', 'he', 'he', 'hey', 'hem'])
        self.assertEqual(task.trie_lookup('hem', t), True)
        self.assertEqual(task.trie_lookup('he', t), True)
        self.assertEqual(task.trie_lookup('h', t), False)
        self.assertEqual(task.trie_lookup('hey', t), True)
        self.assertEqual(task.trie_lookup('yeh', t), False)

        t = build(['he', 'hey', 'hem', 'he', 'hey', 'hem'])
        self.assertEqual(task.trie_lookup('hem', t), True)
        self.assertEqual(task.trie_lookup('he', t), True)
        self.assertEqual(task.trie_lookup('h', t), False)
        self.assertEqual(task.trie_lookup('hey', t), True)
        self.assertEqual(task.trie_lookup('yeh', t), False)

    def test_remove_empty(self):
        t = {}
        task.trie_remove('hi', t)
        self.assertEqual(lookup('hi', t), False)
        self.assertEqual(lookup('h', t), False)
        self.assertEqual(lookup('', t), False)
    def test_remove_one(self):
        t = build(['hi', 'his'])
        task.trie_remove('hi', t)
        self.assertEqual(lookup('his', t), True)
        self.assertEqual(lookup('him', t), False)
        self.assertEqual(lookup('hi', t), False)
        self.assertEqual(lookup('h', t), False)
        self.assertEqual(lookup('', t), False)
    def test_remove_all(self):
        t = build(['hi', 'his'])
        task.trie_remove('hi', t)
        self.assertEqual(lookup('his', t), True)
        self.assertEqual(lookup('him', t), False)
        self.assertEqual(lookup('hi', t), False)
        self.assertEqual(lookup('h', t), False)
        self.assertEqual(lookup('', t), False)
        task.trie_remove('his', t)
        self.assertEqual(lookup('his', t), False)
        self.assertEqual(lookup('him', t), False)
        self.assertEqual(lookup('hi', t), False)
        self.assertEqual(lookup('h', t), False)
        self.assertEqual(lookup('', t), False)

unittest.main(exit=False)