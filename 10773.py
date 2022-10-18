import sys

stack = []

N = int(sys.stdin.readline())

for i in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()


if not stack:
    sys.stdout.write(str(0))
else:
    sys.stdout.write(str(sum(stack)))