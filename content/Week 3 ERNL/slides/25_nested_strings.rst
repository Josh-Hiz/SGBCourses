Concatenating nested strings
============================

Write a function ``nested_concat`` that concatenates the strings in an arbitrarily nested list. It should take a list or string as input, and return a string as output. Our tester will only give you appropriate inputs.

Examples
--------

.. code-block::

    >>> nested_concat([])
    ''
    >>> nested_concat(['hello', 'world'])
    'helloworld'
    >>> nested_concat([[[['help'],'i'],['am', 'stuck'],'in'],'a','list'])
    'helpiamstuckinalist'

.. challenge::
    :tester: /_static/cs515_challenges/Week3/Challenge3/test_task.py

    # define nested_concat here