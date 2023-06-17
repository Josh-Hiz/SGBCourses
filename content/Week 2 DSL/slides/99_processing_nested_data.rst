Processing nested data
======================

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

Now that we know how to access the data in a dictionary of dictionaries, let us see how to solve some simple data processing problems in a dictionary of dictionaries.

**Q1. Write a function that will return the average of the five grade components of the student with a given student_id as the input parameter.**
-------------------------------------------------------------------------------------------------------------------------------------------------

We will first access each of the grade components for the ``student_id`` passed in as the input parameter, we will then proceed to calculate the sum of the grades and then divide the sum by the number of grade components which is 5. Then we will return the value of average thus computed from the function.

.. code-block:: python

    def compute_average(sid):

        # Accessing each grade component
        pa_grade = student_data[sid]['pa']
        rq_grade = student_data[sid]['rq']
        lab_grade = student_data[sid]['lab']
        midterm_grade = student_data[sid]['midterm']
        final_grade = student_data[sid]['final']

        # Summing up the grades of each component 
        sum_of_grades = pa_grade + rq_grade + lab_grade + midterm_grade + final_grade

        # Calculating the average of grade components
        average = sum_of_grades / 5

        return average
    
Now we can call the function with an ``student_id`` as the input parameter as follows:

.. code-block:: 

    >>> print(compute_average('A16771125'))
    82.6

    >>> print(compute_average('A16600612'))
    94.6

**Q2. Write a function that will return the list that contains the student ids of those students who received above 90 in the PAs. The input parameter is the dictionary of dictionaries.**
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

For this function, we pass the dictionary of dictionaries as the input parameter and iterate over the entire dictionary using a for loop and use an if condition to check if the student obtained above 90 in the PA. If the student has obtained above 90, then we will append it to the list we have created before the for loop. In the end, we return the list thus created.

.. code-block:: python

    def is_pa_above_90(student_data):

        # Creating an empty list to store the student ids
        stu_list = []

        # Iterating over each dictionary key
        for stu_id in student_data.keys():

            # Checking if the pa grade is above 90
            if student_data[stu_id]['pa'] > 90:
                # Append to the list if the grade is above 90
                stu_list.append(stu_id)

            else:
                continue

        return stu_list

Now we can call the function with an ``student_data`` as the input parameter as follows:

.. code-block:: 

    >>> print(is_pa_above_90(student_data))
    ['A16771125', 'A16600612', 'A16280707', 'A16740228', 'A16393543']