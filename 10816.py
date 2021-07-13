import sys

N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))

M=int(sys.stdin.readline())
B=list(map(int,sys.stdin.readline().split()))

Hash={}

for i in A:
    if i in Hash:
        Hash[i]+=1
    else:
        Hash[i]=1

for i in range(M):
    if B[i] in Hash:
        print(Hash[B[i]],end=" ")
    else:
        print(0,end=" ")