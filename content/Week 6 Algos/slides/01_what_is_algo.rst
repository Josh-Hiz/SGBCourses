What is an algorithm?
=====================

An **algorithm** is "a finite sequence of well-defined instructions, typically used to solve a class of specific problems or to perform a computation" (per `Wikipedia <https://en.wikipedia.org/wiki/Algorithm>`_). Let's dig in to the definition:

* Algorithms are **finite** and **well-defined**. That is, to be an algorithm, you need to plan in advance---your plan must be concrete and real (i.e., finite and defined for all possible inputs).
* Algorithms are made up of **instructions**. Intent, intuitions, and "general ideas" don't suffice to make an algorithm.
* Algorithms **solve a class of specific problems** or **perform a [mathematical] computation**. Not all code is algorithmic: an algorithm is the code that particularly solves a well-defined problem or computes the answer to a well-defined computation.

One final note: the **"solve"** in the definition of an algorithm is load bearing. To be an algorithm, code should (a) clearly specify what problem it solves, and (b) come with some argument or guarantee that it **actually solves the problem**. Believing and wanting doesn't make it so; the best algorithms come with **a proof of correctness**. Algorithms often also come with a performance analysis---we'll talk about this a bit more.

History
-------

The word algorithm comes from the 9th Century Persian mathematician `Muḥammad ibn Mūsā al-Khwārizmī <https://en.wikipedia.org/wiki/Muhammad_ibn_Musa_al-Khwarizmi>`_, though algorithms for, e.g., long division or finding roots of polynomials (due to the Babylonians) or enumerating primes or computing greatest common divisors (due to the Greeks) existed well before al-Khwārizmī.

Why do we study algorithms?
---------------------------

The primary reason we study algorithms is because algorithms distill our instrumental, "how" knowledge into steps that we can communicate to a computer. Algorithms are the building blocks of our computational world. That alone is good reason to study algorithms! But there are others.

Most code isn't "algorithmic" in the sense of solving a well-defined problem, though that makes it no less important. For example, user interface code isn't solving a well-defined problem---let the user input data is a bit too nebulous---but it's hard to imagine a system with *no* UI code! Similarly, code for taking user input and updating a database isn't particularly algorithmic---though the code that manages the data in the database probably is.

In the developer world, algorithms are high status: they are a marker of achievement and understanding, inasmuch as they are some of the most complex code that we write. Accordingly, some in industry have conflated algorithmic programming with programming skill in general. Whether or not this is a good decision, it's certainly a fact about the world: facility with algorithmic code is a frequent question at technical interviews, `even if they don't correlate with developer success <https://danluu.com/algorithms-interviews/>`_.

Don't write it yourself!
------------------------

Experience writing algorithmic code is excellent, and it's a wonderful feeling to implement an algorithm correctly. This week we'll learn a variety of sorting algorithms and implement them in Python. But: out in the world, you probably shouldn't write your own sorting algorithm, you should use the ``list.sort`` method. Similarly, just use ``random.shuffle`` before writing your own. Why?

First, ``list.sort`` has already been pretty well debugged. It's going to work. Will yours work correctly in all situations?

Second, ``list.sort`` has already been tuned to work efficiently on a variety of systems. The implementors know about the details of Python's list representation, and they'll generally do a good job on a variety of computers and on a variety of inputs.

Third, other Python developers know what ``l.sort()`` will do to ``l`` (sort it in place, returning ``None``). They don't know what ``l = my_qsort(l)`` will do. Sure, it *ought* to sort ``l``. But they won't know the details: does it modify ``l`` in place and return it, or does it return a new list? Does it affect anything else? Does it *work*?

Sometimes implementing your own is the right choice. You have some data with special properties or some other unique needs, and you know that the existing library doesn't meet the need. Great---do it yourself, and then test it to death. Document why you've done it yourself, so that if things change people can make an informed decision about whether to keep your code.

Let's get started!
------------------