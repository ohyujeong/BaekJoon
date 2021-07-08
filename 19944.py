n,m=map(int,input().split())
if (m==1 or m==2):
    print("NEWBIE!")
elif (m!=1,2):
    if(m>n):
        print("TLE!")
    elif(m<=n):
        print("OLDBIE!")