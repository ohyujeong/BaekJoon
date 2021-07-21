import sys

N,S=map(int,sys.stdin.readline().split())
num=list(map(int,sys.stdin.readline().split()))

result=0

def dfs(idx,sum):
    global result
    if idx >= N:
        return
    sum+=num[idx]
    if sum==S:
        result+=1
    dfs(idx+1,sum-num[idx])
    dfs(idx+1,sum)

dfs(0,0)
print(result)






