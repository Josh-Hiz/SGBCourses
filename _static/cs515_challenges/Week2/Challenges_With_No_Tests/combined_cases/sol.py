# define combined_cases(day1_cases, day2_cases)
def combined_cases(day1_cases,day2_cases):
    new_dict = day1_cases.copy() 
    for k in new_dict.keys():
        if k in day2_cases:
            new_dict[k]+=day2_cases[k]
    return new_dict
            
# here are some tests (feel free to add your own)

assert combined_cases({'Texas': 10678, 'Florida': 7459, 'Illinois': 12601}, {'Texas': 13379, 'Florida': 7925, 'Illinois': 11301}) == {'Texas': 24057, 'Florida': 15384, 'Illinois': 23902}

assert combined_cases({'California': 10577, 'New York': 5167}, {'California': 11835, 'New York': 5364}) == {'California': 22412, 'New York': 10531}