import sys

N=int(sys.stdin.readline())
nums=list(map(int,sys.stdin.readline().split()))

result=[]
cnt=0

for j in range(N):
    for i in range(1,nums[j]+1):
        if nums[j]%i==0:
            result.append(i)
            if i==nums[j]:
                if len(result)==2:
                    cnt+=1
                result.clear()


print(cnt)