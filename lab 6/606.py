a = int(input())
b = input().split()
c = list()
for i in range(a):
    b[i] = int(b[i])
    c.append(b[i])
if all(number>=0 for number in c):
    print("Yes")
else:
    print("No")