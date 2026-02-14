"""a = int(input())
b = list(map(int,input().split()))
for i in range(len(b)):
    print(b[i]*b[i],end=' ')"""
a = int(input())
b = input().split()
for i in range(a):
    b[i] = int(b[i])
    print(b[i]**2,end=' ')
