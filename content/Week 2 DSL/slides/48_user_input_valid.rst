User input validation
=====================

Have you ever tried to set a new password, only for it to be rejected because it wasn't long enough? And then maybe you submitted a different password that was long enough, but it still got rejected because it didn't meet some other criteria like containing a capital letter or number, so you tried again? It's interesting to think about how the program underneath all this is operating. How does it know how many times to ask or when to stop? Wanting to repeat some behavior (asking for a password) until some condition is met (a valid password is provided)... sounds like a job for a while loop!

We can use while loops to implement something called **user input validation**, which is the process of reading in user input, checking that it meets some criteria, and if not, repeating the process until valid input is provided by the user.

As a simple example, we can imagine asking a user to input a number between 1 and 10 (inclusive). We'll want to:

1) Ask for input (a number), then
2) Check if the number is between 1 and 10. If it's not, ask the user for input again.

Here is what that might look like (for this example, we will assume that the user does provide an integer as input):

.. runner:: 

    num = int(input("Please enter a number between 1 and 10: "))       # get input, convert to int
    while num < 1 or num > 10:                                         # if num is not between 1 and 10
        num = int(input("Please enter a number between 1 and 10: "))   # ask again and update num

    # once we get here, it means that num now has a valid input value!
    print(num)

Let's trace through with some specific cases below.

**Case 1: User enters a valid number between 1 and 10 on the first try**
First, let's imagine that when the first line is run, the user enters the number 4. What will happen? The while loop condition will be checked:
``num < 1 or num > 10 ---> 4 < 1 or 4 > 10 ---> False or False ---> False``.
The expression evaluates to ``False``, so we never enter the loop body, and just move on with whatever code comes after the loop. This is the behavior we would expect since the user did indeed meet the criterion of providing a number between 1 and 10.

**Case 2: User enters an invalid number a couple times before giving a valid number**

* Imagine the user first enters the number **77**. The while loop condition will evaluate to ``True`` since 77 is greater than 10
* Next, we enter the while loop body and ask the user to provide us with new input. Imagine the user now gives us the number **-13**. (Notice that we're storing the input in the same variable that we're using in the condition. If we instead stored the new input in a new variable, then ``num`` would never change, and we would never exit the loop!).
* Now we return to the loop condition. -13 is less than 1, so we enter the loop again and ask the user for input again. Imagine this time, they provide the number **9**.
* We return to the loop condition again, which evaluates to ``False`` (the user provided valid input), so we exit the loop