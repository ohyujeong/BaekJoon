import sys

N,M=map(int,sys.stdin.readline().split())

result=[]

def Back(depth):
    if depth == M:
        print(*result,sep=' ')
    else:
        for i in range(1,N+1):
            if i not in result:
                result.append(i)
                Back(depth+1)
                result.pop()

Back(0)






