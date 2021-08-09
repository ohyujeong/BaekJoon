import sys
from collections import deque

T=int(sys.stdin.readline())


dx=[1,-1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append([x,y])

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M and martix[nx][ny]==1:
                martix[nx][ny]=0
                q.append([nx,ny])

for _ in range(T):
    M,N,K=map(int,sys.stdin.readline().split())

    martix=[[0]*M for _ in range(N)]

    for i in range(K):
        x,y=map(int,sys.stdin.readline().split())
        martix[y][x]=1

    cnt=0

    for i in range(N):
        for j in range(M):
            if martix[i][j]==1:
                bfs(i,j)
                cnt+=1

    print(cnt)

