def div_check(i):
    for x in range(i+1):
        if x%12==0:
            yield x


a = int(input())
b = div_check(a)
for i in b:
    print(i,end=' ')