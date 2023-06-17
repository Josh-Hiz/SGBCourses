Storing lists in dictionaries
=============================

You may recall that **keys** must be **immutable**. While this is true, there is no such requirement on values! We can use mutable objects like **lists** as values, and it is often very useful to do so.

A practical example is storing email addresses as a dictionary that relates domain names to user names. For example, suppose we have an email address, which is *notaperson@ucsd.edu*. For this email address, *notaperson* is the **username** and is specific to the owner of the account. *ucsd.edu* is the **domain name** and is shared by all people with *ucsd.edu* email addresses. This organization lends itself well to dictionaries, especially when you consider that **usernames** don't have to be unique! Just because there is *notaperson@ucsd.edu* doesn't mean that *notaperson@gmail.com* doesn't exist for example. 

The reason this lends itself well to dictionaries is that there will likely be many **usernames** associated with each **domain name**. 

Let's create a dictionary using **domain names** as keys and a list of **usernames** as values. 

.. code-block:: 

    emails = {"ucsd.edu" : ["annie","joseph","savitha"], 
    "gmail.com" : ["ben10","annie","dio"], 
    "aol.com" : ["joseph", "hotmail", "coda"]}

Notice that ``"annie"`` and ``"joseph"`` are **usernames** that are associated with different **domain names**. So, *annie@gmail.com* and *annie@ucsd.edu* both exist.

Let's explore some things we can do with this dictionary through clever use of the tools we have. First, let's try adding a **username** to the ``"ucsd.edu"`` **domain name**. To add the **username** ``"yeohee"`` to the ``"ucsd.edu"`` **domain**, we can run:

.. code-block:: 

    emails["ucsd.edu"].append("yeohee")

This is a somewhat dense line of code and may look confusing, but it makes more sense if we can break it down. Remember, ``emails["ucsd.edu"]`` will retrieve the **value** associated with the **key** ``"ucsd.edu"``, which is a **list**! So, we can use the ``append`` method directly on this **list** to add an element to it. Try it yourself to get comfortable with the concept. Are there any other methods you think might be useful to manipulate the **values** of this dictionary?

We might also want to print out the values of the dictionary in a presentable way. Just calling ``print(emails)`` at this point will give us this:

.. code-block:: 

    {'ucsd.edu': ['annie', 'joseph', 'savitha', 'yeohee'], 'gmail.com': ['ben10', 'annie', 'dio'], 'aol.com': ['joseph', 'hotmail', 'coda']}

This is certainly correct, but it doesn't represent our information in a way that is very useful to us. Let's instead print out all the items in a particular **domain** in the standard email format (such as *username@domain.com*). For loops are helpful here!

.. code-block:: 

    domain = "gmail.com"
    for username in emails[domain]:
        print(username + "@" + domain)

You can get a lot out of dictionaries if you use them well. Let's get a bit of practice.