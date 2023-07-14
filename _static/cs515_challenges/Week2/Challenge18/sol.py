password = input()
# The line above will get the first password listed in the sample input.
# Implement your while loop below, then print the first valid password.
while len(password) < 8:
    password = input()

print(password)