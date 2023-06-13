Now backwards is talking
========================

Write a function called ``fun_with_lists(lst)`` which takes in one parameter which is a list of strings that form a sentence. The strings that form the sentence are stored in the list in the reverse order. You need to perform the following to make sense of the sentence that the strings stored in the list form:

- Reverse the list (use the reverse method)

- Insert the string 'The' in the beginning of the list (at index 0) (use the insert method)

- Append the string '.' at the end of the list (use the append method)

The function should return the modified list as shown in the sample outputs.

**Sample Input 1:**

.. code-block:: 

    ['round', 'is', 'earth']

**Sample Output 1:**

.. code-block:: 

    ['The', 'earth', 'is', 'round', '.']

**Sample Input 2:**

.. code-block:: 

    ['program', 'world', 'hello']

**Sample Output 2:**

.. code-block:: 

    ['The', 'hello', 'world', 'program', '.']

.. challenge:: 
    :tester: /_static/cs515_challenges/Week2/Challenge11/test_task.py

    # define fun_with_lists