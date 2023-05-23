a=input()

for i in a:

    j=a.index(i)

    if i not in a[j+1:]:

        print(j)

        break

else:

    print(-1)