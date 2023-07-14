number_of_work_hours = int(input())
number_of_paid_hours = int(input())

# add the declaration of is_enough_time here
is_enough_time = number_of_work_hours <= number_of_paid_hours
print(is_enough_time)