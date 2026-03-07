import re

s = input()

p = re.compile(r"\b\w+\b")

a = p.findall(s)

print(len(a))