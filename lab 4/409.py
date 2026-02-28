def pow_of_two(a):
    for i in range(a+1):
        yield 2**i
a = int(input())
b = pow_of_two(a)
for i in b:
    print(i,end=' ')