Lab grades
==========

Let's consider the same dictionary as before. 

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

.. quizdown::

    # How will you access the lab grades of the student with ```student_id = 'A16280707'```?

    - [ ] ```student_data('A16280707')['lab']```
    - [ ] ```student_data['lab']```
    - [ ] ```student_data.get['A16280707'].get['lab']```
    - [ ] ```student_data.get('A16280707')```
    - [x] ```student_data['A16280707']['lab']```
    - [ ] ```student_data.get('lab')```
    - [x] ```student_data.get('A16280707').get('lab')```
    - [x] ```student_data.get['A16280707'].get('lab')```