import sys

li=[]

for i in range(1000):
    for j in range(i+1):
        li.append(i+1)

A,B=map(int,sys.stdin.readline().split())

print(sum(li[A-1:B]))