Organizing Data
================

.. quizdown::

    ## To represent the table given in the previous reading as a dictionary of dictionaries, Can we also use the column ```first_name``` as the key for the outer dictionary as follows?

    ```python
    student_data = {
        'Timothy': {'student_id': 'A16771125', 'last_name': 'Mccarthy', 'pa': 93, 'rq': 61, 'lab': 90, 
                    'midterm': 95, 'final': 74},
        'Regina': {'student_id': 'A16560701', 'last_name': 'Pierce', 'pa': 51, 'rq': 66,  'lab': 47, 
                    'midterm': 97, 'final': 93},
        'Blaine': {'student_id': 'A16891123', 'last_name': 'Simmons', 'pa': 81, 'rq': 73, 'lab': 94, 
                    'midterm': 78, 'final': 84},
        'Clementine': {'student_id': 'A16600612', 'last_name': 'Pierce', 'pa': 96, 'rq': 98, 'lab': 88, 
                    'midterm': 99, 'final': 92},
        'Baxter': {'student_id': 'A16280707', 'last_name': 'Gonzalez', 'pa': 100, 'rq': 100, 'lab': 94, 
                    'midterm': 95, 'final': 97},
        'Yuhan': {'student_id': 'A16740228', 'last_name': 'Wang', 'pa': 98, 'rq': 73, 'lab': 96, 
                    'midterm': 84, 'final': 87},
        'Regina': {'student_id': 'A16790513', 'last_name': 'Sanford', 'pa': 88, 'rq': 90, 'lab': 80, 
                    'midterm': 93, 'final': 95},
        'Rohit': {'student_id': 'A16393543', 'last_name': 'Singh', 'pa': 98, 'rq': 80, 'lab': 80, 
                    'midterm': 83, 'final': 85},
    }
    ```
    1. [ ] No. We cannot use first_name as the key since it is a string.
    2. [ ] Yes. We can create a dictionary as follows as it would not create any proble,s while accessing the data.
    3. [x] No. We could create the dictionary of dictionaries as specified, but it wouldn't work well since the first_name is not unique.
    4. [ ] Yes. We can easily access the entire details associated with a student with the help of the first_name without any mistakes.