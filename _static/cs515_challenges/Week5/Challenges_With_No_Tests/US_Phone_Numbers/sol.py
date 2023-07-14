# define tel as a regular expression that matches US phone numbers
# use repetition, and capture each part of the number
import re

# Get individual parts
tel_1 = r"(\d{3})\-(\d{3})\-(\d{4})"

# Get whole phone number
tel_2 = r"\d{3}\-\d{3}\-\d{4}"

print(re.findall(tel_1, "212-555-1212"))
print(re.findall(tel_2, "212-555-1212"))
