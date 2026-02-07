a = int(input())
b = list(map(int,input().split()))
maximum = 1
for i in range(len(b)):
    if b[i]==max(b):
        maximum = i+1
print(maximum)