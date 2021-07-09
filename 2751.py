import sys

N=int(sys.stdin.readline())

num_list=[]

for i in range(N):
    num=int(sys.stdin.readline())
    num_list.append(num)

result=sorted(num_list)

for i in range(N):
    print(result[i])