def is_even(n):
    return n%2==0

a = int(input())
b = input().split()
c = list()
for i in range(a):
    b[i] = int(b[i])
    c.append(b[i])

d = list(filter(is_even,c))
print(len(d))
