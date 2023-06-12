How to find out if references point to the same object?
=======================================================

You may be wondering how you can tell whether your references are pointing to the same object. To test this, you can use the ``id()`` function. The ``id()`` function takes in an object and returns the **unique id** of that particular object. An id is simply some unique number that is assigned to all objects that are created in Python. This function is only used to show whether references point to the same object. *You do not need to know exactly how it works and you will not be tested on id()*.

The following code defines two lists and prints the id of these two lists.

.. code-block:: 

    list1 = [1, 2, 3]
    list2 = [1, 2, 3]

    print(id(list1))
    print(id(list2))

The following is the output of the above code. Notice that the ids of ``list1`` and ``list2`` are different. This is because ``list1`` and ``list2`` contain references that point to separate objects. Separate objects should have separate id values. Also notice that when you try to run the above code on your machine, the id's are not the same every time the program executes. These id values are only assigned during program execution and are reassigned when you run the program again.

.. code-block:: 

    65011816
    30072968

Now consider the following code where we define ``list2`` = ``list1``. We should expect the id's of ``list1`` and ``list2`` to be the same here because ``list1`` and ``list2`` contain references that point to the same object.

.. code-block:: 

    list1 = [1, 2, 3]
    list2 = list1

    print(id(list1))
    print(id(list2))

The following is the output of the above code. As expected, the id's of ``list1`` and ``list2`` are the same. This is how you can check whether references point to the same object or to different objects. If the ids are the same, the variables contain references to the same object.

.. code-block:: 

    56230024
    56230024