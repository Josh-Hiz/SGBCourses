Dictionary and tuple practice
=============================

.. code-block:: 

    cities = {(32.7157, 117.1611): 'San Diego', (37.7749, 122.4194): 'San Francisco',
              (40.7128, 74.006): 'New York', (30.2672, 97.7431): 'Austin'}

    coordinates = {'San Diego': (32.7157, 117.1611), 'San Francisco': (37.7749, 122.4194),
                   'New York': (40.7128, 74.006), 'Austin': (30.2672, 97.7431)}

.. free-r:: 
    :answer: \'San Francisco\'|\"San Francisco\"
    :regex: true

    # Question 1

    What is ```cities[(37.7749, 122.4194)]```?

.. free-r:: 
    :answer: \(\s*30.2672\s*,\s*97.7431\s*\)
    :regex: true
    
    # Question 2

    What is ```coordinates['Austin']```?

.. free-r:: 
    :answer: \'New York\'|\"New York\"
    :regex: true
    
    # Question 3

    What is ```cities[(40.7128, 74.006)]```?

.. free-r:: 
    :answer: KeyError
    
    # Question 4

    What is ```cities['San Diego']```?