The call stack
==============

The call stack is a mechanism that allows Python to keep track of its location in a program with multiple functions. We've seen the call stack in our "notional machine" on the board. But our *actual machine* has it, too! Generally, a call stack works as follows.

* When a function is called, it is added to the call stack, and begins executing.
* Any functions that are called by another function are added to the top of the stack, and begin executing immediately, pausing the execution of the function that called them.
* When a given function is finished, it is taken off the top of the stack and the next function on the stack continues executing.

Let's define some functions that will help illustrate how this mechanism works.

.. code-block:: python

    def make_breakfast():
        fry_eggs()
        toast_bread()

    def fry_eggs():
        print("Sizzle sizzle")
        return

    def toast_bread():
        wait_for_toaster()
        return

    def wait_for_toaster():
        print("Ding ding!")
        return

    make_breakfast()

What happens when we call ``make_breakfast()``? Let's follow along with the code, and observe the call stack after each step has completed.

1. ``make_breakfast()`` is called.

``make_breakfast()`` gets added to the call stack, and we begin executing ``make_breakfast()``.

Call Stack:

- ``make_breakfast()``


2. ``fry_eggs()`` is called.

``fry_eggs()`` gets added to the the top of the call stack, and we begin executing ``fry_eggs()``. ``make_breakfast()`` is paused until ``fry_eggs()`` is complete.

Call Stack:

- ``fry_eggs()``
- ``make_breakfast()``


3. ``fry_eggs()`` prints and returns.

``fry_eggs()`` prints ``"Sizzle sizzle"`` and returns. ``fry_eggs()`` is removed from the call stack, and the new topmost call, ``make_breakfast()``, resumes execution from where it was paused.

Call Stack:

- ``make_breakfast()``


4. ``toast_bread()`` is called.

``toast_bread()`` gets added to the the top of the call stack, and we begin executing it. ``make_breakfast()`` is paused until ``toast_bread()`` is complete.

Call Stack:

- ``toast_bread()``
- ``make_breakfast()``

   
5. ``wait_for_toaster()`` is called.

``wait_for_toaster()`` gets added to the the top of the call stack, and we begin executing it. ``toast_bread()`` is paused until ``wait_for_toaster()`` is complete.

Call Stack:

- ``wait_for_toaster()``
- ``toast_bread()``
- ``make_breakfast()``

   
6. ``wait_for_toaster()`` prints and returns

``wait_for_toaster()`` prints ``"Ding ding!"`` and returns. ``wait_for_toaster()`` is removed from the call stack, and the new topmost call, ``toast_bread()``, resumes execution from where it was paused.

Call Stack:

- ``toast_bread()``
- ``make_breakfast()``

   
7. ``toast_bread()`` returns.

``toast_bread()`` returns. ``toast_bread()`` is removed from the call stack, and the new topmost call, ``make_breakfast()``, resumes execution from where it was paused.

Call Stack:

- ``make_breakfast()``

   
8. ``make_breakfast()`` returns.

``make_breakfast()`` returns. The call stack is now empty, and the program has completed running.

Call Stack:

(empty)
