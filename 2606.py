import sys

com=int(sys.stdin.readline())
n=int(sys.stdin.readline())

graph=dict()

for i in range(1,com+1):
    graph[i]=[]

for _ in range(n):
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
    visited = [0] * com
    result=[]
    stack=[root]

    while stack:
        m=stack.pop()
        if visited[m-1]==0:
            visited[m-1]=1
            if m not in result:
                result.append(m)
                stack+=sorted(list(set(graph[m])-set(result)),reverse=True)
        else:
            continue

    return result

ans=dfs(graph,1)

print(len(ans)-1)