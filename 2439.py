N=int(input())
star="*"

for i in range(N):
    print(str(star*(i+1)).rjust(N))