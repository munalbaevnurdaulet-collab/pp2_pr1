"""
def sum_odd(a, b):
    sum=0
    for i in range(a,b+1):
        if i%2!=0:
            sum+=i
    return sum
print(sum_odd(2, 5))
"""

"""
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("abc"))
"""
"""
def add(x, y):
    return x+y
def mult(x, y):
    print(x*y)
print(mult(4,5))
"""
"""
def apply(criteria,n):
    return criteria(n)
def is_even(n):
    if n%2==0:
        print(n,end=' ')
    return n%2==0
def is_odd(n):
    if n%2!=0:
        print(n,end=' ')
    return n%2!=0
print(apply(is_even,5))
print(apply(is_even,6))
print(apply(is_odd,5))
"""
"""
def apply(criteria,n):
    count=0
    for x in range(n):
        count+=criteria(x)
    return count

def criteria(x):
    return x%2==x%3

n=int(input())

print(apply(criteria,n))
"""

#Anonymous Functions---Lambda
"""
def do_twice(n, fn):
    return fn(fn(n))
print(do_twice(4,lambda x: x**2))
"""

#Objects
"""
1234 is an instance of the type int
"hello" is an instance of the type str
"""
class Coordinate(object):
    def _init_(self, xval,yval):
        self.x = xval
        self.y = yval
    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

c1 = Coordinate(5)

print(c1.distance())
