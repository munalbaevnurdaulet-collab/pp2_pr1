def squares(n):
    return n*n

a = int(input())
b = input().split()
c = list()
for i in range(a):
    b[i] = int(b[i])
    c.append(b[i])
result = map(squares, c)
print(sum(result))