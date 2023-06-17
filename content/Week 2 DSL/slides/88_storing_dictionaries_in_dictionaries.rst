Storing dictionaries in dictionaries
====================================

As mentioned earlier, **values** in dictionaries *can* be mutable objects. Lists are a very common example of a mutable object, but we can use **any** mutable object as a **value**, including **dictionaries**! It can get a bit confusing rather quickly, but we can use **dictionaries as values** in our dictionary. This may be a little tricky to conceptualize, but it's really not terribly different from using lists of lists. Let's take a look at an example. Suppose we want to create a dictionary with some information about a particular state. Let's use the following:

.. code-block:: 

    california = {"population" : 39512223, "capital" : "Sacramento", "landlocked" : False}

This contains info on the population, capital, and whether it is surrounded on all sides by land. Take note of the fact that **the values are different data types**! Python dictionaries have no requirement for **values** to be the same data type. This can be useful in cases where the information we are storing is diverse in nature, but you must be careful when working with the dictionary so that whatever code you write works with all the datatypes in the dictionary.

This one dictionary is nice, but it might be more helpful to create a **dictionary of dictionaries**. We'll use the state name as a **key**, and a dictionary containing the information above as a **value**. Take a look!

.. code-block:: 

    states = {"California" : {"population" : 39512223, "capital" : "Sacramento", "landlocked" : False},
              "Oregon" : {"population" : 4217737, "capital" : "Salem", "landlocked" : False},
              "Nevada" : {"population" : 3080156, "capital" : "Carson City", "landlocked" : True}}

The uses of the dictionary of dictionaries are apparently when tasked to find some specific information. Suppose we want to print the capital of Nevada? A simple call to ``print(states["Nevada"]["capital"])`` will print out ``Carson City`` as we might expect. It may be helpful to think of this as a **2D dictionary** of sorts. When we access the **value** of this dictionary with ``states[i][j]``, ``i`` is the **key** to the specific state dictionary we are looking at, and ``j`` is the **key** to the information we are looking for.

It may be helpful to visualize this **dictionary of dictionaries** as a table or hierarchical list:

* California
    * population: 3951223
    * capital: Sacramento
    * landlocked: False

* Oregon
    * population: 4217737
    * capital: Salem
    * landlocked: False

* Nevada
    * population: 3080156
    * capital: Carson City
    * landlocked: True

We can think of ``i`` as the outer entry and ``j`` as the entry, very similarly to **2D lists**. Of course, unlike lists, we must use **keys** to access the values we want, rather than **indices**.