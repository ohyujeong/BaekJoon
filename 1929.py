import sys

M,N=map(int,sys.stdin.readline().split())

sieve=[True]*(N+1)

for i in range(2,int(N**0.5)+1):
    if sieve[i]:
        for j in range(2*i,N+1,i):
            sieve[j]=False

for i in range(M,N+1):
    if i>1 and sieve[i]:
        print(i)
