from collections import deque
import sys

N,M,V=map(int,sys.stdin.readline().split())

graph=dict()

for i in range(1,N+1):
    graph[i]=[]
#시작점에 연결된 간선이 없는 경우가 있기때문에, 모든 노드를 key로 만들어줌

for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    if a not in graph:
        graph[a]=[b]
    elif b not in graph[a]:
        graph[a].append(b)
    if b not in graph:
        graph[b]=[a]
    elif a not in graph[b]:
        graph[b].append(a)


def dfs(graph,root):
    visited = [0] * N
    result=[]
    stack=[root]

    while stack:
        n=stack.pop()
        if visited[n-1]==0:
            visited[n-1]=1
            if n not in result:
                result.append(n)
                stack+=sorted(list(set(graph[n])-set(result)),reverse=True)
        else:
            continue

    return result

def bfs(graph,root):
    visited = [0] * N
    result=[]
    queue=deque([root])

    while queue:
        n=queue.popleft()
        if visited[n-1]==0:
            visited[n-1]=1
            if n not in result:
                result.append(n)
                queue+=sorted(list(set(graph[n])-set(result)))
        else:
            continue

    return result

print(*dfs(graph,V),sep=' ')
print(*bfs(graph,V),sep=' ')



