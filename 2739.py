N=int(input())
if N>=1 and N<=9:
    for i in range(9):
        print("%d * %d =" %(N,(i+1)),N*(i+1))