import sys

Edit_left=list(sys.stdin.readline().strip())
Edit_right=[]

N=int(sys.stdin.readline())

for i in range(N):
    command=sys.stdin.readline().strip().split()
    if command[0]=='L':
        if Edit_left:
            Edit_right.append(Edit_left.pop())
    elif command[0]=='D':
        if Edit_right:
            Edit_left.append(Edit_right.pop())
    elif command[0]=='B':
        if Edit_left:
            Edit_left.pop()
    elif command[0]=='P':
        word=command[1]
        Edit_left.append(word)

print("".join(Edit_left+Edit_right[::-1]))