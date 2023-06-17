Tuples as dictionary keys
=========================

So far, we learned that keys have to be immutable and unique. We also saw examples of keys using integers and strings. Another data type we can use as keys is **tuples**. For instance, if we wanted to map some latitude and longitude coordinates to a city, we can map some tuple with the format, ``(latitude, longitude)``, as a key to a string ``city``. Notice that the type of keys are tuples and the values are strings.

.. code-block:: 
    
    cities = {(32.7157, 117.1611): 'San Diego', (37.7749, 122.4194): 'San Francisco',
              (40.7128, 74.006): 'New York', (30.2672, 97.7431): 'Austin'}

Tuples as Values
----------------

Tuples can also be used as values. Instead of creating a dictionary mapping latitude and longitude coordinates to a city, we can do the reverse by mapping a city to a coordinate. Notice that the type of the keys are strings and the values are tuples.

.. code-block:: 

    coordinates = {'San Diego': (32.7157, 117.1611), 'San Francisco': (37.7749, 122.4194),
                   'New York': (40.7128, 74.006), 'Austin': (30.2672, 97.7431)}

Dictionary of Colors
--------------------

Now that we've learned that we can use tuples for keys and values, another dictionary that would be really helpful is a dictionary of colors associated with their tuple values. Below is a colors dictionary that uses the names of the colors, which are strings, as keys that are mapped to their RGB tuple values.

.. code-block:: 

    colors = {'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255), 'yellow': (255, 255, 0),
              'violet': (238, 130, 238), 'orange': (255, 165, 0), 'indigo': (75, 0, 130)}

If we wanted to create a rainbow stripe, we can do so by using the color dictionary we created. This is much more easier to visualize than if we saw a 2D list of RGB tuples.

.. code-block:: 

    rainbow = [[colors['red'], colors['orange'], colors['yellow'], colors['green'], 
                colors['blue'], colors['indigo'], colors['violet']]]