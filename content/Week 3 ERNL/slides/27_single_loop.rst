What can't a single for loop do?
================================

Now that we've learned for loops, we know that we can easily iterate through a list once using a single for loop. 

Consider the following situation. A researcher at UC San Diego Health is trying to gather information about COVID-19 cases in different cities in California. Right now she has a list named ``cases``, in which the number at index 0 is the number of ``cases`` in San Francisco, index 1 corresponds to Santa Barbara, index 2 corresponds to Los Angeles, and index 3 corresponds to San Diego. The researcher cannot see the list ``cases`` directly, so she wants to print out each element in ``cases``. To do this, she can simply use the following code in Python:

.. code-block::

    for i in range(len(cases)):
        print(cases[i]) 

The researcher is happy with what she gets out of the code above. Later, she decides to give 3 of her research assistants a copy of the number of cases in those cities, so the researcher wants to print out the elements in ``cases`` three more times to give to her assistants. She thinks, "hmm, I cannot do this with a single for loop... but wait, I can do this with 3 for loops!" She quickly comes up with the code below:

.. code-block::

    for i in range(len(cases)):
        print(cases[i])

    for i in range(len(cases)):
        print(cases[i])

    for i in range(len(cases)):
        print(cases[i])

The 3 assistants get their copies of the cases and happily continue with their work. But later, another 10 of her colleagues come to her for copies of number of cases. This time, the researcher thinks: I can still do this with 10 for loops, but what if there are 20 more, 30 more or even 100 more? What should I do?

Think for a moment: what can we do to generalize code like this?