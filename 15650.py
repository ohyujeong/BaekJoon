import sys

N,M=map(int,sys.stdin.readline().split())

result=[]
visited=[0]*N


def Back(depth):
    if depth == M:
        print(*result,sep=' ')
    else:
        for i in range(N):
            if visited[i]==0:
                visited[i]=1
                result.append(i+1)
                Back(depth+1)
                result.pop()

                for j in range(i+1,N):
                    visited[j]=0


Back(0)
