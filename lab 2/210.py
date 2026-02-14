"""a = int(input())
b = list(map(int,input().split()))
b.sort()
for i in range(len(b)):
    print(b[len(b)-1-i],end=' ')
"""
a = int(input())
b = input().split()
c = list()
for i in range(a):
    b[i] = int(b[i])
    c.append(b[i])
d = c.sorted()
print(*c)