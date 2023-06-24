Bottom-up Fisher-Yates
======================

The Fisher-Yates implementation on the previous slide goes "top down", i.e., it starts at index ``n-1`` and counts down. Write another version that counts up. Wikipedia has pseudocode for you:

.. code-block:: 

    -- To shuffle an array a of n elements (indices 0..n-1):
    for i from 0 to n−2 do
        j ← random integer such that i ≤ j < n
        exchange a[i] and a[j]

Write some tests to convince yourself you got it right; the 'Mark' button just runs doctest (and so will be green if you don't write any, whether or not your code works!).

.. challenge:: 


    # define fisher_yates as a bottom-up shuffle
