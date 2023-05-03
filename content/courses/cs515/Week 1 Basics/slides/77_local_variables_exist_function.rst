Local variables only exist during function calls
================================================

We learned that local variables that had been created by a function call are forgotten when the function returns. If you call the same function again, the local variables in this call will not remember the values stored in them from the last function call. Let's think about the following example.

.. code-block:: python

    def assign_x(num, first_call):
    if first_call == False:
        print('The value of x is at the second call:', x)
    x = num

assign_x(8, True)
assign_x(9, False)

``assign_x`` function is slightly modified so that it takes another parameter ``first_call``, which is a boolean variable that indicates if it is the first call of ``assign_x`` function. Our example calls ``assign_x`` function twice. The first call assigns ``num=8`` and f``irst_call=True``. In this call, the local variable ``x`` is set as ``x=8``. The second call of ``assign_x`` function now assigns ``num=9`` and ``first_call=False``. Since the condition of ``if`` statement is satisfied for this second call, the ``print`` function will be called. But now have an error:

.. code-block::

    UnboundLocalError: local variable 'x' referenced before assignment

This is because even though the local variable ``x`` had been assigned as ``x=8`` in the previous function call, the value of ``x`` assigned in the previous call is already forgotten when that call was returned! Note that ``x`` created in the second function call is a newly created variable although it is in the same local scope of ``assign_x`` function with the same name as the previous local variable ``x``.

