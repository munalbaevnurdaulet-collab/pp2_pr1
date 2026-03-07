import re

s = input()
p = input()

a = re.split(p, s)

print(",".join(a))