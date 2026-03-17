import re

text = "how-tos and know-hows, 1990s and 2000, Tom and Jerry"

a = re.compile(r"\d+s?")

b = re.findall(a,text)

for i in b:
    print(i,end=' ')
