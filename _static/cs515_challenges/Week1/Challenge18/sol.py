# define get_num_type here
def get_num_type(num):
    if num == 0:
        return 'zero'
    elif num > 0 and num%2!=0:
        return 'positive and odd'
    elif num > 0 and num%2==0:
        return 'positive and even'
    elif num < 0 and num%2!=0:
        return 'negative and odd'
    elif num < 0 and num%2==0:
        return 'negative and even'