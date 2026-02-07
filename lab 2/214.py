"""a = int(input())
arr = input().split()
for i in range(a):
    arr[i]=int(arr[i])
maxcount = 0
count = 0
for i in range(a):
    for j in range(a):
        if(arr[i]==arr[j]):
            count = count+1
    if(maxcount < count):
        maxcount = count
        c = arr[i]
    if(maxcount==count):
        if(c>arr[i]):
            c = arr[i]
    count = 0
print(c)
print(maxcount) 
"""


a = int(input())
b = input().split()
for i in range(a):
    b[i] = int(b[i])
maxcount = 0
count = 0
for i in range(a):
    for j in range(a):
        if b[i] == b[j]:
            count=count+1
    if maxcount < count:
        maxcount = count
        c = b[i]
    if maxcount == count:
        if c > b[i]:
            c = b[i]
    count = 0
print(c)
print(maxcount)
        

        