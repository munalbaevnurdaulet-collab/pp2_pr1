a = int(input())
b = list(map(int,input().split()))
for i in range(len(b)):
    print(b[i]*b[i],end=' ')