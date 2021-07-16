from collections import deque
N,K=map(int,input().split())

q = deque()

for i in range(N):
    q.append(i+1)

i=0

li=[]

while True:
    i+=1
    if i < K and q:
        q.append(q.popleft())
    elif i == K and q:
        li.append(q.popleft())
        i=0
    else:
        break

result="".join(str(li)[1:-1])
print("<",end="")
print(result,end="")
print(">")







