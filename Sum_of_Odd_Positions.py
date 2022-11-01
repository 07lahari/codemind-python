n=int(input())
lst=list(map(int,input().split()))
a=0
for i in range(len(lst)):
    if i%2!=0:
        a+=lst[i]
print((a))
