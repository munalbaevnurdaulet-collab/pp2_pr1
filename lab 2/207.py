"""a = int(input())
b = list(map(int,input().split()))
maximum = 1
for i in range(len(b)):
    if b[i]==max(b):
        maximum = i+1
print(maximum)"""
a = int(input())
b = input().split()
position = 0
for i in range(a):
    b[i] = int(b[i])
for i in range(a):
    if b[i] == max(b):
        position = i + 1
print(position)