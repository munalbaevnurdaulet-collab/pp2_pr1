import re

a = re.compile("12")
b=input()
c=input()
print(bool(re.search(a,""\d\d)))
print(bool(re.search(a,c)))