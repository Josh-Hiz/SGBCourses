Inheritance
===========

Consider the following definitions.

.. code-block:: 

    class A(object):
        def __init__(self):
            self.v = None
        
        def set(self, v):
            self.v = v

        def get(self):
            return self.v

    class B(A):
        def __init__(self):
            self.v = 42

    class C(A):
        def __init__(self):
            print('building a C')
            
        def set(self, v):
            self.v = v * v

.. free-r:: 
    :answer: 10

    # Question 1 

    What is the output of the following snippet?

    ```python
    a = A()
    a.set(10)
    print(a.get())
    ```

.. free-r:: 
    :answer:
        42
        30
        None

    # Question 2 

    What is the output of the following snippet?

    ```python
    b = B()
    print(b.get())
    b.set(30)
    print(b.get())
    b.set(None)
    print(b.get())
    ```

.. free-r:: 
    :answer: building a C\s*AttributeError\s*
    :regex: true

    # Question 3

    What is the output of the following snippet?

    ```python
    c = C()
    print(c.get())
    ```

    >>Since ```C``` override ```__init__```, we never run ```A```'s ```__init__``` when creating ```c```, so ```self.v``` won't be defined (and raises an ```AttributeError``` during ```get```).

.. free-r:: 
    :answer: building a C 400

    # Question 4

    What is the output of the following snippet?

    ```python
    c = C()
    c.set(20)
    print(c.get())
    ```