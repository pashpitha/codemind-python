n=int(input())
c=0
a=list(map(int,input().split()))
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if(i!=j):
            if(a[i]>a[j]):
                c+=1
    print(c,end=' ')