def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a,b=b,a+b
n = int(input())
first = True
for i in fibonacci(n):
    if not first:
        print(",",end='')
    print(i,end='')
    first=False





