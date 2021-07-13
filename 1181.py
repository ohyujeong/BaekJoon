N=int(input())

WordList=[]

for i in range(N):
    word=input()
    WordList.append(word)

result=list(set(WordList))

result.sort()
result.sort(key=len)

for i in range(len(result)):
    print(result[i])