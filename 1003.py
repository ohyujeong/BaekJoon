import sys


T=int(sys.stdin.readline())

zero=[1,0,1]
one=[0,1,1]

def fib(n):
    length=len(zero)
    if n>=length:
        for i in range(length,n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print("%d %d"%(zero[n],one[n]))

for _ in range(T):
    fib(int(sys.stdin.readline()))
