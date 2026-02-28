'''def sum_odd(a,b):
    sum=0
    for i in range(a,b+1):
        if i%2==1:
            sum+=i
    return sum

a,b=map(int,input().split())
print(sum_odd(a,b))'''
'''def add(x,y):
    return x+y
def mult(x,y):
    print(x*y)
add(1,3)
print(add(2,6))
mult(3,4)
print(mult(4,5))'''
"""def calc(op,x,y):
    return op(x,y)
def div(x,y):
    if y!=0:
        return x/y
    print("y = 0")

x,y=map(int,input().split())
result = calc(div,x,y)
print(result)"""
def is_even(i):
    return i%2==0
a = int(input())
print(is_even(a))
print(lambda a: a%2==0)
