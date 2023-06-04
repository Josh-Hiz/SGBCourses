Part 5: Input and Output
========================

So far, we've been providing some code in the background of the challenges that reads in the input, sets up variables, then runs your code and prints the results. This section shows you the functions we used to do that, which you will use frequently for the rest of the quarter.

The relevant functions are:

``input()`` or

``input()`` or ``input(s)``

Shows the prompt ``s`` (if given), and waits for the user to give some input. It reads the input up until they press enter/return (or there's a new line in the input), and returns the result as a string.

``print(v)``

Takes any value v and prints it out. If ``v`` is a string, it prints the string without surrounding quotes.

Now that we have these functions, we can start running our code in earnest. Here's an example: we'll read in two strings on separate lines in the input and then print them out separated by a comma.

.. runner::

    str1 = input()
    str2 = input()
    combined = str1 + "," + str2
    print(combined)

When you click the **Run** button, a cursor will appear in a box below the code. If you type ``a``, hit enter, then ``b``, and hit enter, the program will print out ``a,b``. Try it again with other inputs!