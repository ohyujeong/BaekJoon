import sys
from collections import deque

deq=deque()

N=int(sys.stdin.readline())

for i in range(N):
    command=sys.stdin.readline().strip().split()
    if command[0]=='push_front':
        num=int(command[1])
        deq.appendleft(num)
    elif command[0]=='push_back':
        num = int(command[1])
        deq.append(num)
    elif command[0]=='pop_front':
        if not deq:
            print(-1)
        else:
            print(deq.popleft())
    elif command[0]=='pop_back':
        if not deq:
            print(-1)
        else:
            print(deq.pop())
    elif command[0]=='size':
        print(len(deq))
    elif command[0]=='empty':
        if not deq:
            print(1)
        else:
            print(0)
    elif command[0]=='front':
        if not deq:
            print(-1)
        else:
            print(deq[0])
    elif command[0]=='back':
        if not deq:
            print(-1)
        else:
            print(deq[-1])
