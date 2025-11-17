What is an object?
==================

An **object** is a value that combines code and data together. It can be very useful to have code and data bundled like this: an object lets us have a family of functions with shared state. The data part of an object (i.e., its state) is held in **members** or **fields**; the code part of an object is held in **methods**. These are just fancy names for data and code, in a particular context. **Object-oriented programming** or **OOP** refers to programming that makes essential use of objects. Python is a versatile programming language that supports OOP, among other paradigms.

Our motivating example will be a **counter**. A counter is two things: some state (how many things have been counted) and ways to work with it (increment it, check its current value, etc.). You could achieve a counter using the ``global`` keyword---we've already done that, in fact. But an object lets you bundle the state with the counter logic, which means you don't have to rely on global state at all!

In Python, every object has a **class**---that is, it has a **type**. For example, ``5`` has type ``int`` and ``'howdy'`` has type ``str`` and ``[True, False, None]`` has type ``list``. The type ` In Python, the words 'type' and 'class' are synonymous---not so every other language.