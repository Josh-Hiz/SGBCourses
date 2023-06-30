Dictionaries within dictionaries
================================

.. code-block:: 

    states = {"California" : {"population" : 39512223, "capital" : "Sacramento", "landlocked" : False},
              "Oregon" : {"population" : 4217737, "capital" : "Salem", "landlocked" : False},
              "Nevada" : {"population" : 3080156, "capital" : "Carson City", "landlocked" : True}}

Let's get a bit of practice. Using the ``states`` dictionary above, give the output for each code snippet.

In case of a KeyError, give the key that was missing, i.e., ``KeyError: 'foo'``.

.. free-r:: 
    :answer: 39512223

    # Question 1

    ```
    states["California"]["population"]
    ```

.. free-r:: 
    :answer: \'Salem\'|\"Salem\"
    :regex: true

    # Question 2

    ```
    states['Oregon']['capital']
    ```

.. free-r:: 
    :answer: True

    # Question 3

    ```
    states["Nevada"]["landlocked"] or states["Oregon"]["landlocked"]
    ```

.. free-r:: 
    :answer: False

    # Question 4

    ```
    states["California"]["landlocked"]
    ```

.. free-r:: 
    :answer: KeyError:\s*(\'capital\'|\"capital\")
    :regex: true

    # Question 5

    ```
    states['capital']['California']
    ```

.. free-r:: 
    :answer: KeyError:\s*(\'Connecticut\'|\"Connecticut\")
    :regex: true

    # Question 6

    ```
    states["Connecticut"]["population"]
    ```

.. free-r:: 
    :answer: KeyError:\s*(\'area\'|\"area\")
    :regex: true

    # Question 7

    ```
    states['Oregon']['area']
    ```

.. free-r:: 
    :answer: 3080156

    # Question 8

    ```
    states['Nevada']['population']
    ```

.. free-r:: 
    :answer: 3080156

    # Question 8

    ```
    states['Nevada']['population']
    ```

.. free-r:: 
    :answer: \'Carson City\'|\"Carson City\"
    :regex: true
    
    # Question 9

    ```
    states['Nevada']['capital']
    ```