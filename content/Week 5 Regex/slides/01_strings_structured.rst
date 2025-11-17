Turning strings into structured things
======================================

We frequently need to find things in strings. We've learned ``'a' not in "silly"`` and ``'abc' in "crabcake"`` the like to find out whether a string is a substring of another, but it's a very common programming task to take in a string and produce some kind of structured output. Here are some examples:

* Taking a URL and determining the protocol to use and domain to contact.
* Taking an email and determining the domain to contact and the user to send to.
* Turning a configuration file into a runtime configuration.
* Looking through DNA bases to find patterns (e.g., two ``A`` bases followed by anything followed by a ``T`` base).
* Loading Python code and running it.

In general, the process of taking a string and producing a structured output is called **parsing**. Parsing is an old, complex, and beautiful topic. This week, we'll learn about the simplest possible parsing regime, called **regular expressions**, and see how we can use them to achieve simple parsing tasks.