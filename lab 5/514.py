import re

a = input()

b = re.compile(r"^[0-9]*$")

if re.search(b,a):
    print("Match")
else:
    print("No match")

