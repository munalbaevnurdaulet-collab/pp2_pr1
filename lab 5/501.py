import re

a = input()

b = re.compile(r"^Hello")

if re.match(b,a):
    print("Yes")
else:
    print("No")