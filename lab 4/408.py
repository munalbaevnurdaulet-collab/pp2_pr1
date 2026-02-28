def prime_num(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def generator_prime(n):
    for i in range(2,n+1):
        if prime_num(i):
            yield i

a = int(input())
for i in generator_prime(a):
    print(i,end=' ')