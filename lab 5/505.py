import re

a = input()

b = re.compile(r"^[a-Z]*[0-9]+$")


if re.search(b,a):
    print("Yes")
else:
    print("No") 