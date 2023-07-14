# define print_numbers
def print_numbers(lst):
    for item in lst:
        if item % 3 == 0:
            continue
        print(item)