import re

s = input()

a = re.findall(r"\w+", s)

print(len(a))