import re

s = input()

a = re.findall(r"[A-Z]", s)

print(len(a))