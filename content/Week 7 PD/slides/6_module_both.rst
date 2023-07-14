Get you a module that can do both
=================================

Define a module ``sort`` (i.e., a file ``sort.py``) with the definition ``mergesort``. 

When ``sort`` is invoked as a main module, you should read a line of input, split it on whitespace (i.e., ``s.split()`` with no argument), sort it using ``mergesort``, and print out the sorted list. That is:

.. code-block::

    [user@sahara ~]$ python -m sort
    hello there old friend
    ['friend', 'hello', 'old', 'there']

The ``sort`` code should do nothing when it's just imported. To test this out, define a module ``client`` that imports ``sort`` and sorts the letters of the string "antidisestablishmentarianism". For example:

.. code-block::

    [user@sahara ~]$ python client.py
    ['a', 'a', 'a', 'a', 'b', 'd', 'e', 'e', 'h', 'i', 'i', 'i', 'i
    ', 'i', 'l', 'm', 'm', 'n', 'n', 'n', 'r', 's', 's', 's', 's', 
    't', 't', 't']