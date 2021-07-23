import sys

result=[]

n=int(sys.stdin.readline())

def hanoi(n,start,end,mid):
    global result

    if n==1:
        result.append([start,end])
    else:
        hanoi(n-1,start,mid,end)
        result.append([start,end])
        hanoi(n-1,mid,end,start)
    return result

hanoi(n,1,3,2)
print(len(result))

for x,y in result:
    print(x,y)