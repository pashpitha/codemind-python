from collections import Counter

a=list(input())

b=dict(Counter(a))

x=b.get('z')

y=b.get('o')

if 2*x==y:

    print('Yes')

else:

    print('No')