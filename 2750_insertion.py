N=int(input())

Nums=[]

for i in range(N):
    Nums.append(int(input()))

def insertion_sort(data):
    for i in range(len(data)-1):
        key=data[i+1]
        j=i
        while j>=0 and data[j]>key:
            data[j+1]=data[j]
            j-=1
        data[j+1]=key

insertion_sort(Nums)

for i in range(N):
    print(Nums[i])
