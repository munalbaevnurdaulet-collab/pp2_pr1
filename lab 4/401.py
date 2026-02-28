def squares(i):
    for x in range(1,i+1):
        yield x*x
a = int(input())
c = squares(a)
for i in c:
    print(i)
