import re

s = input()
p = input()

p = re.escape(p)

a = re.findall(p, s)

print(len(a))