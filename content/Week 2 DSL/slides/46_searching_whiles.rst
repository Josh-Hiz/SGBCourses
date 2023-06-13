Searching with while loops
==========================

We've searched through a list in the "Finding something in a list" challenge, using for loops. And we've also met the ``in`` operator. We can *also* use while loops to iterate over a list and check if it contains something we're interested in. For example, say we had a list of integers and wanted to know if any of the elements are negative. It's possible to use a for loop for that, but ``in`` would be tricky. Then, we could do something like the following:

.. runner:: 

    my_list = [1, 6, -8, 2, 11]
    contains_negative = False              # whether we've found a negative number
    index = 0                              # index to use to iterate through my_list

    # if we haven't found a negative number yet and still
    # haven't reached the end of my_list, check the next element
    while not contains_negative and index < len(my_list):
        if my_list[index] < 0:
            contains_negative = True
        index += 1
    print(index, contains_negative)

Let's break down the pieces of this:

* We use the ``index`` variable to keep track of the current index in ``my_list`` that we're going to check, and we use ``contains_negative`` to store whether or not we have found a negative number in ``my_list``.
* The loop body checks whether or not the element at ``my_list[index]`` is negative or not, and updates ``contains_negative`` accordingly. Then, it increments ``index`` so in the next (potential) iteration of the loop, the next index of ``my_list`` will be checked
* The loop continues iterating until the loop condition is ``False``, which happens when either ``contains_negative`` is ``True`` or ``index`` >= the length of ``my_list``

This loop will keep iterating until ``contains_negative`` is updated to be ``True`` when ``-8`` at index 2 is determined to be negative. Once ``contains_negative`` changes to ``True``, ``index`` is then incremented and we check the loop condition again. The condition will evaluate to ``False`` because ``not contains_negative`` evaluates to ``False``, and so we exit the loop.

What if, instead, our list was the following:

.. code-block:: python

    my_list = [1, 6, 8, 2, 11]

Since we don't have any negative numbers, the loop will instead exit when ``index`` is no longer smaller than the length of the list (``index < len(my_list)`` evaluates to ``False``). This is why we need this second loop condition. If we didn't have it, the loop would continue and try to access an index that's out of bounds of the list.

Common mistake: off-by-one errors
----------------------------------

But wait, if we want to check the *whole* list, why are we checking if ``index < len(my_list)`` instead of ``index <= len(my_list)``? This is because if we had instead used ``<=``, we would be trying to check one element too many. Recall that the last valid index of a list is one less than the length of a list (e.g. the index of the last element of ``my_list`` is 4, but its length is 5). We would have gone through the loop body *one more* time than we should have if we used ``<=``. This is a very common type of mistake to make, and is classified as an **off-by-one error**, because we would have been off by one from the correct number of times we should have executed the loop. Off-by-one errors often occur due to logical errors in loop conditions, so stay on your toes!