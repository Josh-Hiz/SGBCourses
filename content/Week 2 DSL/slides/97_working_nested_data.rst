Working with nested data
========================

Let us consider the previously described dictionary of dictionaries.

.. code-block:: 

    student_data = {
        'A16771125': {'first_name': 'Timothy', 'last_name': 'Mccarthy', 'pa': 93, 'rq': 61, 'lab': 90, 
                      'midterm': 95, 'final': 74},
        'A16560701': {'first_name': 'Regina', 'last_name': 'Pierce', 'pa': 51, 'rq': 66,  'lab': 47, 
                      'midterm': 97, 'final': 93},
        'A16891123': {'first_name': 'Blaine', 'last_name': 'Simmons', 'pa': 81, 'rq': 73, 'lab': 94, 
                      'midterm': 78, 'final': 84},
        'A16600612': {'first_name': 'Clementine', 'last_name': 'Pierce', 'pa': 96, 'rq': 98, 'lab': 88, 
                      'midterm': 99, 'final': 92},
        'A16280707': {'first_name': 'Baxter', 'last_name': 'Gonzalez', 'pa': 100, 'rq': 100, 'lab': 94, 
                      'midterm': 95, 'final': 97},
        'A16740228': {'first_name': 'Yuhan', 'last_name': 'Wang', 'pa': 98, 'rq': 73, 'lab': 96, 
                      'midterm': 84, 'final': 87},
        'A16790513': {'first_name': 'Regina', 'last_name': 'Sanford', 'pa': 88, 'rq': 90, 'lab': 80, 
                      'midterm': 93, 'final': 95},
        'A16393543': {'first_name': 'Rohit', 'last_name': 'Singh', 'pa': 98, 'rq': 80, 'lab': 80, 
                      'midterm': 83, 'final': 85},
    }

Let's try how we can solve the following questions with the help of what we have learned about dictionaries so far.

**Q1. Print the details of the student with the student_id = 'A16790513'.**
---------------------------------------------------------------------------

There are two ways you solve this problem as shown below:

.. code-block:: 

    # Using the given key directly
    print(student_data['A16790513'])

    # Using the get method 
    print(student_data.get('A16790513'))

Since ``student_data`` is a dictionary we can access the contents by providing the key directly within square brackets or by using the get method of dictionaries. Both the above statements will print the same details as given below:

.. code-block:: 

    {'first_name': 'Regina', 'last_name': 'Sanford', 'pa': 88, 'rq': 90, 'lab': 80, 'midterm': 93, 'final': 95}

**Q2. Print the marks obtained by the student with the student_id = 'A16393543' in the reading quiz**
-----------------------------------------------------------------------------------------------------

There are two ways you solve this problem as shown below:

.. code-block::

    # Using the given keys directly
    print(student_data['A16393543']['rq'])

    # The above is same as doing:
    # student_details_dict = student_data['A16393543']
    # rq_grade = student_details_dict['rq']
    # print(rq_grade)

.. code-block:: 

    # Successively using the get method 
    print(student_data.get('A16393543').get('rq'))

    # The above is same as doing:
    # student_details_dict = student_data.get('A16393543')
    # rq_grade = student_details_dict.get('rq')
    # print(rq_grade)

Since ``student_data`` is a dictionary we can access the contents by providing the key directly within square brackets as **'A16393543'** or by using the ``get`` method. This will yield a dictionary containing the details of that student. So we in turn again apply the same method to access contents within this inner dictionary. We can either use the key **rq** directly or we can use the ``get`` method.