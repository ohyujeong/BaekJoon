from itertools import combinations
import sys

while True:

    S=list(map(int,sys.stdin.readline().split()))
    if S[0]==0:
        break
    S.pop(0)

    Lotto=list(combinations(S,6))
    for i in Lotto:
        for j in i:
            print(j,end=" ")
        print()
    print()


