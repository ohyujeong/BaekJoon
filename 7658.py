N = int(input())
peopleList = []

for _ in range(N):
    weight, height = map(int, input().split())
    peopleList.append((weight, height))

for i in peopleList:
    rank = 1
    for j in peopleList:
        #peopleList[i][0] [i][1], peopleList[j][0] [j][1]
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank,end = " ")