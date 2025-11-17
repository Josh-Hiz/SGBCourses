Constructors
============

.. free-r:: 
    :answer:
        Hello!
        Hello!
        Hello!

    # Question 1

    What will the following code snippet output?

    ```python
    class C(object):
        def __init__(self):
            print('Hello!')
            
    C()
    C()
    C()
    ```

.. free-r:: 
    :answer:
        Hello, Mother!
        Hello, Father!

    # Question 2

    What will the following code snippet output?

    ```python
    class D(object):
        def __init__(self, name):
            print(f'Hello, {name}!')
            
    D('Mother')
    D('Father')
    ```
