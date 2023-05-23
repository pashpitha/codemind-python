a=list(map(list,input().split()))

for i in range(len(a)):

    if a[i][0] in ['a','e','i','o','u','A','E','I','O','U']:

        a[i].append('ma')

    else:

        t=a[i][0]

        a[i].pop(0)

        a[i].append(t)

        a[i].append('ma')

    a[i].append('a'*(i+1))

for i in range(len(a)):

    b="".join(a[i])

    print(b,end=" ")