def countdown(a):
    while(a>=0):
        yield a
        a=a-1

a = int(input())
b = countdown(a)
for i in b:
    print(i)
