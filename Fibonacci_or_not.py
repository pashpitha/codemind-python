n=int(input())
a,b=0,1,
for i in range(n):
    if(a==n):
        break
    a,b=b,a+b
print(a==n)