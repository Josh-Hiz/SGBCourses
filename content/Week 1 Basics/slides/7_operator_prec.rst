Operator Precedence
===================

In Python, when multiple operators appear within the same expression, there is an order in which the different operators will be evaluated. The operators and the order (or precedence) in which they will be evaluated are shown in the table below. Operators in the same row have the same precedence and they are evaluated from left to right (based on the order they appear in the expression).

.. list-table:: Operators
    :widths: 25 25 50
    :header-rows: 1

    * - Order/Precedence
      - Operator
      - Description
    * - 1
      - ()
      - Parenthesis
    * - 2
      - `**`
      - Exponentiation
    * - 3
      - `*`, /, //, %
      - Multiplication, Division, Integer Division, Modulus
    * - 4
      - +,-
      - Addition, Subtraction 

Consider the following expression that has multiple operators.

.. code-block:: python

        >>> 5 + 7 % 2 * 3
        8

In the example above, the operators ``%`` and ``*`` will be evaluated first since they have a higher precedence when compared to the operator ``+``. As the two operators ``%`` and ``*`` are the same precedence level, they will be evaluated from left to right. That is, ``%`` will be evaluated first and then ``*`` will be evaluated. The way the expression will be evaluated is shown below.

``5 + 7 % 2 * 3`` will become ``5 + 1 * 3`` which in turn will become ``5 + 3`` which will produce the final result of ``8``. You may have learned rules like PEMDAS---the rules here are essentially the same.

NB that we haven't talked about division in detail---we'll do more with that next week.