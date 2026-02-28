def even_nums(i):
    for x in range(i+1):
        if x%2==0:
            yield x 

a = int(input())
c = even_nums(a)
first = True
for i in c:
    if not first:
        print(",",end='')
    print(i,end='')
    first=False
