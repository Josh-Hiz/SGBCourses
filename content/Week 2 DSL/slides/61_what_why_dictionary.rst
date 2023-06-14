What and why are dictionaries?
==============================

So far we've learned that we can represent a collection of data using lists. While lists work well for certain tasks, they also have some limitations. For instance, let's say we want to find the mode from a list of integers. Recall that the mode is the number that appears most often in a set of numbers. How would we count the number of occurrences for each number? While we can use a list to keep track of the counts, we still have to keep track of the numbers that correspond to the counts. Is there a better way to implement this? In this lesson, we will learn another way we can represent a collection of data in Python.

What are Dictionaries?
----------------------

Like a list, a **dictionary** is a mutable collection of many values. But unlike indices for lists, indices for dictionaries can use many different data types, not just integers. Indexes for dictionaries are called **keys**, and a key with its associated **value** is called a **key-value pair**. Compared to lists, dictionaries have no order. We will further discuss this concept in a later step.

Why is this datatype called a dictionary? You can imagine that each entry in an actual dictionary is a word and its definition. When we look up an entry, we essentially look up a word and find its definition. Similarly, a Python dictionary is used to look up a key and it's corresponding value.