import re

s = input()

a = re.findall(r"\b\w{3}\b", s)

print(len(a))