import sys


def DFS(depth,root):
    if depth == 6:
        print(*result,sep=' ')
    else:
        for i in range(root,k):
            if visited[i]==0:
                result[depth]=test[i]
                visited[i]=1
                DFS(depth+1,i+1)
                visited[i]=0

while True:
    test = list(map(int, sys.stdin.readline().split()))
    k = test.pop(0)

    if k==0:
        break

    visited = [0] * k
    result = [0] * 6

    DFS(0,0)
    print()


