a=int(input())
b=int(input())
for i in range (a,b+1):
    x=i
    y=0
    z=0
    while(x!=0):
        d=x%10
        x=x//10
        y+=1
        if(d==0):
            break
        if(i%d==0):
            z+=1
    if(z==y):
        print(i,end=' ')
