"""a = int(input())
b = list(map(int,input().split()))
print(max(b))"""
a = int(input())
b = input().split()
c = list()
for i in range(a):
    b[i] = int(b[i])
    c.append(b[i])
print(max(c))
    
