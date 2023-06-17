Finding the mode in a list of numbers
=====================================

In this lesson, we will discuss more ways to use dictionaries. Let's return to the motivation of finding the mode of a series of numbers. Recall that the mode is the number that appears most often in a set of numbers. Now that we've learned about dictionaries, how can we use it to find the mode in a list of numbers?

We can break the process of finding the mode into two tasks. The first task is to find out the number of occurrences for each number. The second task is to use that information to find the number that occurs most often.

**Recording the Number of Occurrences**
---------------------------------------

Let's tackle the first task of keeping track of the number of occurrences for each number by using a dictionary. Each key will be a number in the list and each value will be the count of that number. We can read through each number in the list while continuously updating our dictionary.

.. code-block:: python

    nums = [5, 5, 6, 4, 7, 8, 5, 6] # A list of numbers for which we want to find the mode

    counts = {} # Create an empty dictionary
    for num in nums: # loop through each number in nums
        if num in counts: # Check if num is a key in counts
            counts[num] += 1 # increment the count of nums by 1
        else:
            counts[num] = 1 # Set the count of num to 1

    print(counts)

Our code prints out the following dictionary. Our dictionary indicates that we have 3 fives, 2 sixes, 1 four, 1 seven, and 1 eight which are the correct counts from the list ``nums``.

.. code-block:: python

    {5: 3, 6: 2, 4: 1, 7: 1, 8: 1}

**Finding the Most Common Number**
----------------------------------

Now let's tackle the second task and find the key with the most counts. One way to implement this is to iterate through every key and value in the dictionary and find the maximum value and its corresponding key.

Recall from the previous lesson that the ``items()`` function will return a collection of every pair in the dictionary, where each pair is a **tuple** of a key and a value. The first element in the tuple is the key and the second is the value. 

``max_key`` and ``max_value`` are used to keep track of the current maximum value. Whenever we find a value greater than ``max_value``, we update that key-value pair to be the new ``max_key`` and ``max_value``.

.. code-block:: python

    max_key = 0 # initialize the key that corresponds to the max value
    max_value = 0 # initialize the max value
    for pair in counts.items(): # pair is a tuple
        key = pair[0]
        value = pair[1]
        if value > max_value: # If value is greater than the current max value
            max_value = value # Update the new max_value
            max_key = key # update the new max_key

    print("mode =", max_key)

Our second half of the code prints out the following which is correct since 5 is the most common number.

.. code-block:: python

    mode = 5