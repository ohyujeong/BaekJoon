import sys
from collections import deque

N,M=map(int,sys.stdin.readline().split())

martix=[]
for _ in range(N):
    martix.append(list(map(int,sys.stdin.readline().strip())))

dx=[1,-1,0,0]
dy=[0,0,-1,1]
visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]

def bfs():
    queue = deque()
    queue.append([0,0,1])
    visit[0][0][1]=1

    while queue:
        x,y,z=queue.popleft()

        if x==N-1 and y==M-1:
            return visit[x][y][z]

        for i in range(4):
            nx=x + dx[i]
            ny=y + dy[i]

            if nx>=0 and nx<N and ny>=0 and ny<M:
                if martix[nx][ny]==0 and visit[nx][ny][z]==0:
                    visit[nx][ny][z]=visit[x][y][z]+1
                    queue.append([nx,ny,z])
                elif martix[nx][ny]==1 and z==1:
                    visit[nx][ny][0]=visit[x][y][1]+1
                    queue.append([nx,ny,0])
    return -1


print(bfs())