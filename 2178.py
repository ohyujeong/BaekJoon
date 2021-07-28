import sys

N,M=map(int,sys.stdin.readline().split())

martix=[]
for _ in range(N):
    martix.append(list(map(int,sys.stdin.readline().strip())))

dx=[1,-1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=[(x,y)]
    while queue:
        x,y=queue.pop(0)

        for i in range(4):
            nx=x + dx[i]
            ny=y + dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<M:
                if martix[nx][ny]==1:
                    martix[nx][ny]=martix[x][y]+1
                    queue.append((nx, ny))

    return martix[N-1][M-1]


print(bfs(0,0))
