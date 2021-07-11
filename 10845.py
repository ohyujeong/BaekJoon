import sys

Queue=[]

N=int(sys.stdin.readline())

for i in range(N):
    command=sys.stdin.readline().strip().split()
    if command[0]=='push':
        num=int(command[1])
        Queue.append(num)
    elif command[0]=='pop':
        if not Queue:
            print(-1)
        else:
            print(Queue[0])
            Queue.pop(0)
    elif command[0]=='size':
        print(len(Queue))
    elif command[0]=='empty':
        if not Queue:
            print(1)
        else:
            print(0)
    elif command[0]=='front':
        if not Queue:
            print(-1)
        else:
            print(Queue[0])
    elif command[0]=='back':
        if not Queue:
            print(-1)
        else:
            print(Queue[-1])

