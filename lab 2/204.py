count = 0
a = int(input())
b = list(map(int,input().split()))
for i in range(len(b)):
    if b[i] > 0:
        count=count+1
print(count)
    