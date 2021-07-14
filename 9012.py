T=int(input())

for i in range(T):
    stack = []
    pl=input()
    check=0
    for j in pl:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if not stack:
                print("NO")
                check=1
                break
            else:
                stack.pop()
    if not stack and check == 0:
        print("YES")
    elif stack and check == 0:
        print("NO")


