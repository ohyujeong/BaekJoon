import sys

N=int(sys.stdin.readline())

Nums=[[0]*2 for _ in range(N)]

for i in range(N):
    Nums[i]=list(map(int,sys.stdin.readline().split()))

Nums.sort(key=lambda x:(x[1],x[0]))

for x,y in Nums:
    print(x,y)