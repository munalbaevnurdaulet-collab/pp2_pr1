def limited_c(a,n):
    for i in range(n):
        for item in a:
            yield item
a = input().split()
b = int(input())
for i in limited_c(a,b):
    print(i,end=' ')