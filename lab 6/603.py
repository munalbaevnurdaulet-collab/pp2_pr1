a = int(input())
b = input().split()
c = list()
for i in range(a):
    c.append(b[i])

for i, words in enumerate(c):
    print(f"{i}:{words}",end=' ')