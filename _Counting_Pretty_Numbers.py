n=int(input())
for  i in range (0,n):
    a,b=map(int,input().split())
    c=0
    for j in range(a,b+1):
        rem=j%10
        if(rem==2 or rem==3 or rem==9):
            c+=1
    print(c)