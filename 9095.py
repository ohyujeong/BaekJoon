import sys

T=int(sys.stdin.readline())

def solve(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return solve(n-1)+solve(n-2)+solve(n-3)

for i in range(T):
    n=int(sys.stdin.readline())
    print(solve(n))

