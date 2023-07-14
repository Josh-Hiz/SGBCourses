# you need this line to get math.sqrt
import math

# read a float from the user and print out its square root
while True:
    try:
        s = input('Enter a floating point number: ')
        n = float(s)
        if n >= 0:
            break
        print(f"'{n}' doesn't have a (real) square root.")
    except ValueError:
        print(f"'{s}' is not a floating point number.")
print(f"The square root of {n} is {math.sqrt(n)}.")