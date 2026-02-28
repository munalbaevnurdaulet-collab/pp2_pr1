a = int(input())
b = input().split()
c=[]
for i in range(a):
    b[i]=int(b[i])
    c.append(b[i])
print(c.count(c[0]))
