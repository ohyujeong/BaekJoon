import sys

N=int(sys.stdin.readline())

cnt=0

for i in range(1,N+1):
    if i<100:
        cnt+=1
    else:
        numlist=list(map(int,str(i)))
        if numlist[0]-numlist[1] == numlist[1] - numlist[2]:
            cnt+=1

print(cnt)