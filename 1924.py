x,y=map(int,input().split())

Week=["SUN","MON","TUE","WED","THU","FRI","SAT"]
Month=[31,28,31,30,31,30,31,31,30,31,30,31]
Day=0

for i in range(x-1):
    Day += Month[i]

Day=(Day+y)%7
print(Week[Day])



