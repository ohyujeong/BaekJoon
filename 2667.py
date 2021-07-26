import sys

N=int(sys.stdin.readline())

martix=[]
for _ in range(N):
    martix.append(list(map(int,sys.stdin.readline().strip())))

dx=[1,-1,0,0]
dy=[0,0,-1,1]
cnt=0
result=[]

def dfs(x,y):
    global cnt
    if x>=N or x<0 or y>=N or y<0:
        return False

    if martix[x][y]==1:
        cnt+=1
        martix[x][y] = 0

        for i in range(4):
            dfs(x+dx[i],y+dy[i])

        return True
    return False

for i in range(N):
    for j in range(N):
        search=dfs(i,j)
        if search:
            result.append(cnt)
            cnt=0

result.sort()

print(len(result))
for i in result:
    print(i)
