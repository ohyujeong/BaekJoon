import sys
from collections import deque

M,N=map(int,sys.stdin.readline().split())

q=deque()
dx=[1,-1,0,0]
dy=[0,0,-1,1]

martix=[list(map(int,sys.stdin.readline().split()))for _ in range(N)]

for i in range(N):
    for j in range(M):
        if martix[i][j]==1:
            q.append([i,j])

def BFS():
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0 <= nx < N and 0 <= ny < M and martix[nx][ny] == 0:
                if martix[nx][ny]==0:
                    q.append([nx, ny])
                    martix[nx][ny]=martix[x][y]+1

BFS()

check = False
result = -2

for i in martix:
    for j in i:
        if j == 0:
            check= True
        result = max(result, j)

if check:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)


