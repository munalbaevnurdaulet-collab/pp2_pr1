a = int(input())
c = list()
d = list()
for i in range(a):
    b = input()
    c.append(b)
count = 0
count2 = 0
for i in range(a):
    for j in range(a):
        if c[i] == c[j]:
            count = count+1
    if c[i] not in d:
        if count == 3:
            count2= count2 + 1
        d.append(c[i])
    count = 0
print(count2)



