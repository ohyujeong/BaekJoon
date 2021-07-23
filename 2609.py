import sys

a,b=map(int,sys.stdin.readline().split())

def gcd(x,y):
    while y:
        x,y=y,x%y
    return x

def lcm(x,y):
    result=(x*y)//gcd(a,b)
    return result

print(gcd(a,b))
print(lcm(a,b))