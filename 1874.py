import sys

n=int(sys.stdin.readline())

stack=[]
result=[]
check=0
i=1

for _ in range(n):
    num=n=int(sys.stdin.readline())
    while i<=num:
        stack.append(i)
        result.append('+')
        i+=1
    if stack[-1]==num:
        stack.pop()
        result.append('-')
    else:
        check=1
        print('NO')
        break

if check==0:
    for j in result:
        print(j)





