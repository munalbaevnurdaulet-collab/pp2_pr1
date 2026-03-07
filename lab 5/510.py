import re

a = input()

b = re.compile(r"(cat|dog)")
if re.search(b,a):
    print("Yes")
else:
    print("No")