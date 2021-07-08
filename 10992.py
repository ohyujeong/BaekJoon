N=int(input())

star='*'

for i in range(1,N+1):
    if(i==1 or i==N):
        a=' ' * (N-i) +star*(2*i-1)
        print(a)
    else:
        a=' '*(N-i) +star+' '*(2*(i-1)-1)+star
        print(a)

