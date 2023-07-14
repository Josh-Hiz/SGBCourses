directory = [{'first_name': 'James', 'last_name': 'Smith', 'phone_number': 5106423175, 'state': 'CA'},
{'first_name': 'Jennifer', 'last_name': 'Wilson', 'phone_number': 5307521011, 'state': 'OR'},
{'first_name': 'Robert', 'last_name': 'Jones', 'phone_number': 9498245011, 'state': 'NY'},
{'first_name': 'Mary', 'last_name': 'Willaims', 'phone_number': 3108254321, 'state': 'TX'},
{'first_name': 'John', 'last_name': 'Brown', 'phone_number': 2092284400, 'state': 'CA'},
{'first_name': 'Patricia', 'last_name': 'Miller', 'phone_number': 9518271012, 'state': 'FL'},
{'first_name': 'Jennifer', 'last_name': 'Davis', 'phone_number': 8585342230, 'state': 'CA'},
{'first_name': 'Linda', 'last_name': 'Johnson', 'phone_number': 4153537800, 'state': 'GA'}]

# define lookup_state(state)
def lookup_state(state):
    lst = []
    for dictionary in directory:
        if dictionary['state'] == state:
            lst.append(dictionary['first_name'] + " " + dictionary['last_name'])
    return lst
# a test to make things easy for you
assert lookup_state('CA') == ['James Smith', 'John Brown', 'Jennifer Davis']