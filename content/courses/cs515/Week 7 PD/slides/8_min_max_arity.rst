Variable arity minimum and maximum
==================================

In Python, the ``min`` and ``max`` functions are variable arity:

.. exec_code::

    print(min(3,2,1,0))
    print(max(*range(0,100)))

Define your own versions of these funtions---call them ``minimum`` and ``maximum``. They should raise a ``TypeError`` if called with 0 or 1 arguments; if called with 2 or more arguments, they should calculate the minimum or maximum appropriately. Here's an example interaction:

.. code-block::


    >>> maximum(1,2,3,4)
    4
    >>> minimum(1,2,3,4)
    1
    >>> maximum(*range(0,1000))
    999
    >>> maximum()
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: maximum() missing 2 required positional arguments: '
    first' and 'second'
    >>> minimum(1)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: minimum() missing 1 required positional argument: 's
    econd'
    >>> minimum(1,2)
    1

(Look at ``help(min)`` for info on how the real, Python versions of these functions work---they're a little more complicated than what we're asking for.)

**Access the challenge 4 folder and nothing else**


.. jupyterlite::
   :width: 100%
   :height: 800px
   :prompt: Begin!
   :prompt_color: #cd46e8