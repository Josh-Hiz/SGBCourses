print_emails
============

In this challenge, you will write a function to print out all of the emails in the ``emails`` dict from last lesson. For your reference:

.. code-block:: 

    emails = {"ucsd.edu" : ["annie","joseph","savitha"], 
    "gmail.com" : ["ben10","annie","dio"], 
    "aol.com" : ["joseph", "hotmail", "coda"]}

Write a function named ``print_emails`` that takes as a parameter a **dictionary of lists** where all **values** are lists of strings and prints all the emails contained within in the form *username@domain.com*. This function will only be tested on the ``emails`` dictionary. The emails should be printed in the order shown in the sample test case.

Your function will automatically be run on the ``emails`` dictionary above.

Your function does not need to **return** anything, so you can leave the ``return`` in the function alone. Rather, this function should **print** an email of the form *username@domain.com* for each string in each list, a total of **9** emails.

**Sample Input:**

.. code-block:: python

    emails = {"ucsd.edu" : ["annie","joseph","savitha"], "gmail.com" : ["ben10","annie","dio"], "aol.com" : ["joseph", "hotmail", "coda"]}

**Sample Output:**

.. code-block::

    annie@ucsd.edu
    joseph@ucsd.edu
    savitha@ucsd.edu
    ben10@gmail.com
    annie@gmail.com
    dio@gmail.com
    joseph@aol.com
    hotmail@aol.com
    coda@aol.com

.. challenge::
    :tester: /_static/cs515_challenges/Week2/Challenge22/test_task.py

    # define print_emails(emails)