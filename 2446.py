N=int(input())

for i in range(N):
    a=' '*i+'*'*(2*(N-i)-1)
    print(a)

for j in range(2,N+1):
    a=' '*(N-j)+'*'*((2*j)-1)
    print(a)