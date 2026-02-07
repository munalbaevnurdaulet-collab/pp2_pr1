minimum = 0
a = int(input())
b = list(map(int,input().split()))

max = max(b)
min = min(b)

for i in range(a):
    if b[i] == max:
        b[i] = min
print(*b)




