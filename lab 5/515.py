import re

s = input()

def f(m):
    d = m.group()
    return d + d

print(re.sub(r"\d", f, s))