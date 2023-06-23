Regular expressions: a better way
=================================

Suppose you had 100 motifs to look for. Writing 100 functions---one for each motif---would be tedious and error-prone. We need a better way to express patterns in sequnces!

**Regular expressions** are a powerful tool for expressing patterns. Given a regular expression, there efficient an uniform algorithms for searching text and matching parts of it against the pattern.

Regular expressions are also called **regexes**, and they're available in Python using the re module. Python's regular expression support is good, with a fast engine for searching ("does this string contain this pattern?"), matching ("given this abstract pattern, what are the concrete instances in this string?"), and substitution ("automatically alter the string by changing according to this pattern").

Some examples of what we can do with a regular expression:

* Identify valid IP addresses
* Identify words that start with 'a' and have more then 5 letters
* Break up an email string like 'Michael Greenberg <mgreenbe@stevens.edu>' into the parts 'Michael Greenberg' and 'mgreenbe@stevens.edu'
* Search and replace every occurrence of 'Bob' with 'Robert'
* Search and replace every occurrence of 'X machine' and replace it with 'X computer' (for any word X)
* Transform 'Greenberg, Michael Matthew' into 'Michael Matthew Greenberg'
* Count the occurrences of words that end in 'ization'
  
The remainder of today's readings and exercises will teach you the basics of regular expressions and Python's ``re`` library.
