"""a = int(input())
b = list(map(int,input().split()))

max = max(b)
min = min(b)

for i in range(a):
    if b[i] == max:
        b[i] = min
print(*b)


"""

a = int(input())
c = list()
b = input().split()
for i in range(a):
    b[i] = int(b[i])
    c.append(b[i])
for i in range(a):
    if c[i] == max(c):
        c[i] = min(c)
print(*c)

