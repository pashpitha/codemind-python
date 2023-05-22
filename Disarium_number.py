n=input()
j,sum=1,0
for i in n:
    sum+=int(i)**j
    j+=1
print(sum==int(n))