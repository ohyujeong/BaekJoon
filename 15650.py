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

                for j in range(i+1,N): # 1,2 / 2,1 이런 중복 허용x니까 i는 계속 방문했다고 체크함
                    visited[j]=0


Back(0)
