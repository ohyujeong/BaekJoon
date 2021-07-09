N=int(input())
A=list(map(int,input().split()))

M=int(input())
B=list(map(int,input().split()))

list.sort(A)

def binary_search(start,end,data,x):
    if start > end:
        return 0

    mid=(start+end)//2

    if data[mid]==B[x]:
        return 1
    elif data[mid]>B[x]:
        end=mid-1
    else:
        start=mid+1

    return binary_search(start,end,A,x)

for i in range(M):
    print(binary_search(0,len(A)-1,A,i))
