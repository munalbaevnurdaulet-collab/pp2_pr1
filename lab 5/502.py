import re

a = input()

b = input()

c = re.compile(b)
if re.search(c,a):
    print("Yes")
else:
    print("No")