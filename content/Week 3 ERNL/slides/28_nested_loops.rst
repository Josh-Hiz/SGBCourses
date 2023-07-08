Nested for loops
================

The researcher cannot come up with an idea to gracefully solve this problem, so she goes to her friend who is a tutor for CSE 8A at UC San Diego for help. Her friend replies, "Haha, this is when a true computer scientist shines!" Then she provides the following code:

.. code-block::

    for i in range(n):
        for j in range(len(cases)):
            print(cases[j])

where ``n`` is the number of copies she needs. 

The researcher applies the code above, and surprisingly, it works!

The code above contains a structure called a "**nested for-loop**" because it is a loop *inside* a loop. WHAT?!!! Can you do that?!

Oh yes, you absolutely can! 

How do nested for-loops work?
-----------------------------

We've seen for-loops before:

.. code-block::

    for i in range(3):
        print('Hello World!')

This will unroll to:

.. code-block::

    print('Hello World!')
    print('Hello World!')
    print('Hello World!')

**Nested for-loops** unroll the same way!

Let's say ``n = 3``. Then the code snippet the researcher's friend provides above becomes:

.. code-block::

    for i in range(3):
        for j in range(len(cases)):
            print(cases[j])

This will unroll to:

.. code-block::

    for j in range(len(cases)):
        print(cases[j])

    for j in range(len(cases)):
        print(cases[j])

    for j in range(len(cases)):
        print(cases[j])
    
*(each for loop above will also unroll)*

which is the exact same code the researcher came up on her own before for printing copies for her 3 assistants!

For a simple for-loop, its job is to repeatedly execute codes within it. For nested for-loops, the **outer for-loop**'s job is the same: repeatedly execute code within it! However, this time, code within the outer for-loop contains another for-loop! The for-loop within the o**uter for-loop** is called **inner for-loop**. 

It's easy to see that the **inner for-loop** is just a regular simple for-loop, but there is also nothing special about the **outer for-loop**: it's also a regular simple for-loop! Both the **inner** and the **outer for-loops** are just doing their basic job: repeatedly execute code within them.

But when we use structure like nested for-loops, they can provide us many more functionalities (like iterate through 2D lists and images which we will learn later) than just simple non-nested for-loops.